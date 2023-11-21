"""Command Line  Interface for Crewcal, a tool that extracts flight data from an airline crew schedule."""
import pathlib

import click
from halo import Halo

from crewcal import schedule
from crewcal.llm_extract import OpenAISchedule


@click.group()
def cli():
    """Crewcal is a tool that extracts flight data from an airline crew schedule.

    An LLM (Large Language Model) is used to extract data from the unstructured schedule
    (in pdf format). This data is then converted to iCalendar format (or alternatively
    a crewcal specific json file) and saved to a specified file.

    Note that the an environment variable named "OPENAI_API_KEY" must be set
    with your OpenAI API key. At present (november 2023) each 'extract' costs just
    under USD 0.01 (charged to your OpenAI account).
    """


@click.command
@click.option(
    "--overwrite",
    "-o",
    is_flag=True,
    help="Overwrite the iCalendar file if it already exists.",
)
@click.argument("json")
@click.argument("ical")
def convert(json: str, ical: str, overwrite: bool) -> int:
    """Convert crewcal json schedule file to iCalendar file.

    The JSON file should be in crewcal json format.

    \b
    Args:
        JSON (str): Path to json file containing schedule.
        ICAL (str): Path to iCalendar file.
    """  # noqa: D301
    json_path = pathlib.Path(json)
    ical_path = pathlib.Path(ical)

    if not ical_path.suffix:
        ical_path = ical_path.with_suffix(".ics")

    if ical_path.is_file() and not overwrite:
        click.echo(
            f"File {ical_path} already exists. Consider using '--overwrite' option."
        )
        return -1

    if not json_path.is_file() and not json_path.with_suffix(".json").is_file():
        click.echo(f"User specified file '{json_path}' not found.")
        return -1

    if not json_path.is_file():
        json_path_modified = json_path.with_suffix(".json")
        click.echo(
            f"File '{json_path}' not found. Using '{json_path_modified}' instead."
        )
        json_path = json_path_modified

    sched = schedule.Schedule.from_json(json_path)
    sched.to_icalendar_file(ical_path)

    return 0


@click.command
@click.option(
    "--to-json",
    "-j",
    is_flag=True,
    help="Save to crewcal json schedule file (instead of Icalendar).",
)
@click.option(
    "--overwrite",
    "-o",
    is_flag=True,
    help="Overwrite the target file if it already exists.",
)
@click.argument("sourcefile")
@click.argument("targetfile")
def extract(sourcefile: str, targetfile: str, to_json: bool, overwrite: bool) -> int:
    """Extract schedule from pdf file and save to iCalendar format (or json).

    The saved json is in a format specific to crewcal. If saved to json,
    use 'crewcal convert' to convert it to iCalendar format.

    \b
    Args:
        SOURCEFILE (str): Path to pdf file.
        TARGETFILE (str): Path to iCalendar (or json) file.
    """  # noqa: D301
    out_path = pathlib.Path(targetfile)
    source_path = pathlib.Path(sourcefile)

    if not (out_path.suffix):
        out_path = out_path.with_suffix(".json" if to_json else ".ics")

    if out_path.is_file() and not overwrite:
        click.echo(
            f"File '{out_path}' already exists. Consider using '--overwrite' option."
        )
        return -1

    if not source_path.is_file() and not source_path.with_suffix(".pdf").is_file():
        click.echo(f"User specified file '{source_path}' not found.")
        return -1

    if not source_path.is_file():
        source_path_modified = source_path.with_suffix(".pdf")
        click.echo(
            f"File '{source_path}' not found. Using '{source_path_modified}' instead."
        )
        source_path = source_path_modified

    with Halo(
        text="Extracting schedule, saving to iCalendar format.", spinner="dots"
    ) if not to_json else Halo(
        text="Extracting schedule, saving to crewcal json format.", spinner="dots"
    ):
        sched = (
            OpenAISchedule(schedule_path=source_path, to_icalendar_file=out_path)
            if not to_json
            else OpenAISchedule(schedule_path=source_path, to_json_file=out_path)
        )

    click.echo(f"Extracted schedule saved to {out_path}.")

    del sched

    return 0


cli.add_command(convert)
cli.add_command(extract)

if __name__ == "__main__":
    cli()
