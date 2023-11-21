"""Entry point for crewcal package command line interface.

Convert an airline crew schedule pdf into iCalendar format.
"""

import logging

from crewcal import schedule


def main():
    """_summary_."""
    sched = schedule.Schedule.from_json("sched.json")

    logging.warning(sched.to_icalendar().serialize())

    sched.to_icalendar_file("schedule3.ics")

    logging.warning(sched.json_dumps())

    return -1


if __name__ == "__main__":
    main()
