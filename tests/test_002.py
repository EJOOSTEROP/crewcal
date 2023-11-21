import unittest

import pendulum
from crewcal.schedule import Schedule


class TestEvent(unittest.TestCase):
    def setUp(self):
        self.event = Schedule.from_json().events[0]
        self.event.end_date = "2022-01-01"
        self.event.list_times = ["12:00", "13:00", "14:00"]
        self.event.destination_timezone = ["America/New_York", "America/Los_Angeles"]

    def test_get_end(self):
        expected_datetime = pendulum.datetime(
            2022, 1, 1, 14, 0, tz="America/Los_Angeles"
        )
        assert self.event.get_end() == expected_datetime


if __name__ == "__main__":
    unittest.main()
