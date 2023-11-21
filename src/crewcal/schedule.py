"""Classes defining a flight schedule for an airline crew member.

The schedule is a list of events, each of which contains the details of a set of flight.

"""
import json
import logging
from pathlib import Path
from typing import List

import ics
import pendulum
from pydantic import BaseModel, Field, TypeAdapter


class Event(BaseModel):
    """The details of a flight on a flight schedule for an airline crew member."""

    starting_date: str
    starting_time: str
    duties: List[str]
    summary: str
    description: str
    departure_airport: List[str]
    departure_airport_name: List[str]
    departure_timezone: List[str] = Field(description='for example "America/Toronto"')
    destination_airport: List[str]
    destination_airport_name: List[str]
    destination_timezone: List[str]
    end_date: str
    end_time: str
    crew_list: List[str]
    list_times: List[str]
    list_airport_codes: List[str]

    def list_airport_pairs(self):
        """Generate a formatted string of airport pairs."""
        airport_pairs = zip(
            self.duties, self.departure_airport_name, self.destination_airport_name
        )
        formatted_pairs = (
            f"{flight_num}: {dep} - {dest}" for flight_num, dep, dest in airport_pairs
        )
        return "\n".join(formatted_pairs)

    def get_description(self):
        """Generate a formatted string of flight event details.

        Returns:
            str: description
        """
        return "\n".join(
            [
                self.list_airport_pairs(),
                *self.crew_list,
                f"\nFlight ends in {self.destination_timezone[-1]} timezone.",
            ]
        )

    def get_begin(self):
        """Get the starting time of the flight event.

        Returns:
            datetime: start datetime
        """
        return pendulum.from_format(
            f"{self.starting_date} {self.starting_time}",
            "YYYY-MM-DD HH:mm",
            tz=self.departure_timezone[0],
        )

    def get_end(self):
        """Get the ending time of the flight event.

        Returns:
            datetime: end datetime
        """
        return pendulum.from_format(
            f"{self.end_date} {self.list_times[-1]}",
            "YYYY-MM-DD HH:mm",
            tz=self.destination_timezone[-1],
        )


class Schedule(BaseModel):
    """A flight schedule for an airline crew member."""

    events: List[Event]

    def to_icalendar(self):
        """Generates a iCalendar representation of the schedule.

        Returns:
            ics.Calendar: The iCalendar object containing the events.
        """
        calendar = ics.Calendar(creator="Ternyx - crewcal")

        events = [
            ics.Event(
                name=flight.summary,
                description=flight.get_description(),
                begin=flight.get_begin(),
                end=flight.get_end(),
            )
            for flight in self.events
        ]
        calendar.events.update(events)

        return calendar

    def to_icalendar_file(self, filename: str) -> None:
        """Write the iCalendar representation of the schedule to a file.

        Parameters:
            filename (str): The name of the file to write the iCalendar data to.
        """
        try:
            with Path(filename).open("w") as f:
                f.write(self.to_icalendar().serialize())
        except Exception as e:
            logging.warning(f"Error writing to file: {e}")

    def json_dumps(self, indent=2):
        """Show the schedule as a JSON string.

        Parameters:
            indent (int):

        Returns:
            str: The JSON representation of the schedule.
        """
        return json.dumps(self.model_dump(mode="json"), indent=indent)

    @staticmethod
    def from_json(filename: str = "./etc/sched.json") -> "Schedule":
        """Load flight events from a JSON file and create a schedule.

        Args:
            filename (str): The path of the JSON file.

        Returns:
            Schedule: A Schedule object containing the schedule of flights.
        """
        with Path(filename).open("r") as openfile:
            events_from_file = json.load(openfile)

        adapter = TypeAdapter(List[Event])
        events = adapter.validate_python(events_from_file)
        return Schedule(events=events)

    @staticmethod
    def from_json_string(json_string: str) -> "Schedule":
        """Load flight events from a JSON string and create a schedule.

        Args:
            json_string (str): The events in JSON format.

        Returns:
            Schedule: A Schedule object containing the schedule of flights.
        """
        adapter = TypeAdapter(List[Event])
        events = adapter.validate_python(json_string)
        return Schedule(events=events)
