"""Prompts for the LLM."""

template_flight_schedule = """
Your task is to convert the information I will provide into a list of calendar events.

The information contains a list of duties for an airline crew member. Duties consist of one or more flights. You will represent each duty as a calendar event.

The section with Hotel Information contains no new events. Instead it contains the hotel at destination for some of the flights.

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
- Arrival date. A '+1' means the next day. Only capture yyyy-mm-dd format.
- Arrival time, the last occurrence of a time for each day. A '+1' means the next day. Only capture HH:mm format.
- List of crew members
- A list of all times found. Only capture HH:mm format.
- List of all airport codes.
- Hotel information at destination. Obtain this from the document section 'Hotel Information'. It includes the name, full address and phone number of the hotel at destination. For some flights this does not exist. In that case keep this part empty.

Always include all items in your output even if they are empty.
"""


template_hotel_contacts = """
The provided document may contain a section with hotel information, base your answer on this section.

The hotel section may contain information about one or more hotels.
For each hotel, provide:
- a suggested file name for the vcf file (vCard format).
- the contact information of the hotel, in vCard format.

If you cannot find any hotel contact information, return an empty list.
"""
