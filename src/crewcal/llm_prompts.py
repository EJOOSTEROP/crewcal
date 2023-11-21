"""Prompts for the LLM."""

template_flight_schedule = """
Your task is to convert the information I will provide into a list of calendar events.

The information contains a list of duties for an airline crew member. Duties consist of one or more flights. You will represent each duty as a calendar event.

Ignore the section with Hotel Information.

Each event contains the following items:
- Departure date in yyyy-mm-dd format
- Departure time in HH:mm format
- Duties which contains one or multiple flight numbers
- Summary which contains the origin and departure airports
- Origin airport code. Sometimes multiple flights exist. Capture all origin airports.
- Origin airport name
- Origin timezone in ISO 8601 format (for example 'America/Toronto')
- Destination airport code
- Destination airport name
- Destination timezone
- Arrival date
- Arrival time, the last occurrence of a time for each day
- List of crew members
- A list of all times found
- List of all airport codes
"""
