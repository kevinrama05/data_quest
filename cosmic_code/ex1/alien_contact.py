from enum import Enum
from pydantic import BaseModel, Field, model_validator
from datetime import datetime


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def contact_id_validation(self) -> "AlienContact":
        if self.contact_id[:2] != "AC":
            raise ValueError("Contact ID start with 'AC' (Alien Contact)")
        return self

    @model_validator(mode="after")
    def physical_contact_verified(self) -> "AlienContact":
        if self.contact_type == "physical":
            if self.is_verified is False:
                raise ValueError("Physical contact reports must be verified")
        return self

    @model_validator(mode="after")
    def telepathic_contact_report(self) -> "AlienContact":
        if self.contact_type == "telepathic":
            if self.witness_count < 3:
                raise ValueError(
                        "Telepathic contact requires at least 3 witnesses"
                )
        return self

    @model_validator(mode="after")
    def strong_signal(self):
        if self.signal_strength > 7:
            if self.message_received is None:
                raise ValueError(
                    "Strong signals (> 7.0) should include received messages"
                )

        return self


def display_contact(contact: AlienContact) -> None:
    status = "Verified" if contact.is_verified else "Unverified"
    print(f"ID:        {contact.contact_id}")
    print(f"Type:      {contact.contact_type.value}")
    print(f"Location:  {contact.location}")
    print(f"Signal:    {contact.signal_strength}/10")
    print(f"Duration:  {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Status:    {status}")
    if contact.message_received:
        print(f"Message:   '{contact.message_received}'")


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 38)

    print("Valid contact report:")
    valid_contact = AlienContact(
        contact_id="AC_2024_001",
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True,
    )
    display_contact(valid_contact)

    print("=" * 38)

    print("\nExpected validation error:")
    try:
        test0 = AlienContact(
            contact_id="AC_2024_002",
            location="Roswell, New Mexico",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=20,
            witness_count=1,
            is_verified=False,
        )
        display_contact(test0)
    except Exception as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))

    print("=" * 38)

    print("\nExpected validation error:")
    try:
        test = AlienContact(
            contact_id="AC_2024_003",
            timestamp=datetime(2024, 6, 17, 8, 0, 0),
            location="Tunguska, Russia",
            contact_type=ContactType.PHYSICAL,
            signal_strength=3.0,
            duration_minutes=120,
            witness_count=10,
            is_verified=False,
        )
        display_contact(test)
    except Exception as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))

    print("=" * 38)

    print("\nExpected validation error:")
    try:
        test2 = AlienContact(
            contact_id="AC_2024_004",
            timestamp=datetime(2024, 6, 18, 14, 0, 0),
            location="Bermuda Triangle",
            contact_type=ContactType.VISUAL,
            signal_strength=9.5,
            duration_minutes=60,
            witness_count=3,
            is_verified=True,
        )
        display_contact(test2)
    except Exception as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
