"""Read an airline crew schedule in pdf format.

Read the schedule from a pdf file using LLM with OpenAI
to extract flight details in a structured format.

About 0.75 US cents per call in OpenAI API costs.
"""
import json
import logging
import os
from pathlib import Path

import openai
from dotenv import find_dotenv, load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.output_parsers.openai_functions import JsonKeyOutputFunctionsParser
from langchain.prompts import ChatPromptTemplate
from langchain.utils.openai_functions import convert_pydantic_to_openai_function

from crewcal.llm_prompts import template_flight_schedule
from crewcal.schedule import Schedule

_ = load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]


class OpenAISchedule:
    """Extracts flight data from an airline crew schedule provided in PDF format.

    Uses an LLM for extraction. Exctracted data is in a structured format.
    """

    schedule_path: str
    extracted_schedule: str = ""

    def __init__(
        self, schedule_path: str, to_json_file: str = "", to_icalendar_file: str = ""
    ) -> None:
        """Sets up the object using the provided schedule_path. Additionally, it allows for an optional to_file path where the schedule can be extracted.

        If the to_file path isn't specified during object creation, you'll need to call the extraction method explicitly at a later time.

        Sample uses:
        - sched = OpenAISchedule("schedule.pdf", to_json_file="schedule.json") - to extract data from a PDF file and save it to a JSON file
        - sched.write_icalendar("schedule.ics") - to save he previously extract data to an iCalendar file
        - sched.write_json("schedule.json") - to save the extracted data to a JSON file (note that this already happened in the first example)

        - sched = OpenAISchedule.from_json("schedule.json") - create object from JSON. Note that extract() has no functionality and schedule path is empty.
        - sched.write_icalendar("schedule.ics")

        - sched = OpenAISchedule("schedule.pdf")
        - sched.extract()
        - sched.write_icalendar("schedule.ics")

        - sched = OpenAISchedule("schedule.pdf", to_icalendar_file="schedule.ics") - to extract data from a PDF file and save it to a JSON file

        Parameters:
            schedule_path (str): The path to the schedule PDF file.
            to_json_file (str, optional): The path to the file where the schedule will be extracted.
            to_icalendar_file (str, optional): The path to the file where the iCalendar representation of the schedule will be saved.

        Returns:
            None
        """
        self.schedule_path = schedule_path

        if to_json_file:
            self.extract(to_json_file)

        if to_icalendar_file:
            if not self.extracted_schedule:
                self.extract()
            self.write_icalendar(to_icalendar_file)

    def extract(self, to_file: str = "") -> None:
        """Uses LLM to extract event data from a schedule PDF file and optionally saves it to a JSON file.

        Parameters:
            to_file (str, optional): The path to the output JSON file. If not provided, the extracted data will not be saved.

        Returns:
            None
        """
        full_sched_doc = self.read_schedule_pdf(self.schedule_path)

        if full_sched_doc:
            model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
            prompt = ChatPromptTemplate.from_messages(
                [("system", template_flight_schedule), ("human", "{input}")]
            )

            schedule_extraction_function = [
                convert_pydantic_to_openai_function(Schedule)
            ]

            extraction_model = model.bind(
                functions=schedule_extraction_function,
                function_call={"name": "Schedule"},
            )

            extraction_chain = (
                prompt
                | extraction_model
                | JsonKeyOutputFunctionsParser(key_name="events")
            )

            logging.warning(
                "WARNING - This script costs 0.75 US cents per call in OpenAI API costs."
            )

            self.extracted_schedule = extraction_chain.invoke({"input": full_sched_doc})

        if to_file:
            self.write_json(to_file)

    def read_schedule_pdf(self, filepath: str = "") -> str:
        """Reads the contents of a schedule PDF file and returns as a document for an LLM input.

        Args:
            filepath (str): The path to the PDF file.

        Returns:
            str: The concatenated text of all pages in the PDF file.
        """
        if filepath:
            loader = PyPDFLoader(str(filepath))
            documents = loader.load()
            full_sched_doc = "".join([doc.page_content for doc in documents])
        else:
            full_sched_doc = ""

        return full_sched_doc

    def json_dumps(self) -> str:
        """Returns the JSON representation of the schedule in a basic formatted string.

        Returns:
            str: The JSON representation of the schedule.
        """
        return json.dumps(self.extracted_schedule, indent=2, ensure_ascii=False)

    def write_json(self, filepath: str = "./sched.json") -> None:
        """Writes the JSON representation of the schedule to a file."""
        with Path(filepath).open("w") as outfile:
            json.dump(self.extracted_schedule, outfile)

    def write_icalendar(self, filepath: str) -> None:
        """Writes the iCalendar representation of the schedule to a file."""
        sched = Schedule.from_json_string(self.extracted_schedule)
        sched.to_icalendar_file(filepath)
        del sched

    @staticmethod
    def from_json(filepath: str) -> "OpenAISchedule":
        """Initializes a new OpenAISchedule object from a JSON file.

        Args:
            filepath (str): The path to the JSON file.

        Returns:
            OpenAISchedule: The initialized OpenAISchedule object.
        """
        with Path(filepath).open("r") as openfile:
            extracted_schedule = json.load(openfile)

        new_schedule = OpenAISchedule("")
        new_schedule.extracted_schedule = extracted_schedule
        return new_schedule


# TODO: Crew member names are captured, but not seniority and function.
# TODO: Must be asynchronous somehow as OpenAI may take a while to respond.
