"""Class(es) defining contact information for hotels."""

from typing import List

from pydantic import BaseModel, Field


class Hotel(BaseModel):
    """Contact details of a hotel on a flight schedule for an airline crew member."""

    vcf_file_name: str = Field(
        description="Proposed file name for the vCard file, including file extension."
    )
    hotel_contact: str = Field(
        description='Full contact information in vCard format. Phone numbers use the "+ country code" format; do not include "tel" in the phone number. Country is always included. Always include an N record (a structured representation of the name) and an FN record. Include the hotel name in the ORG record. Always include the categories: hotel, crew. Ensure it is compatible with iOS, gmail, Android, Windows and MAC.'
    )


class Hotels(BaseModel):
    """List of hotel information."""

    hotels: List[Hotel]
