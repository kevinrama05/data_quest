from enum import Enum, auto
from pydantic import BaseModel, Field, ValidationError, model_validator
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

    @model_validator(mode='after')
    def contact_id_validation(self):
        if self.contact_id[:2] != "AC":
            raise ValueError("Contact ID start with 'AC' (Alien Contact)")
        return self

    @model_validator(mode='after')
    def physical_contact_verified(self):
        if self.contact_type == "physical":
            if self.is_verified is False:
                raise ValueError("Physical contact reports must be verified")
        return self
    
    @model_validator(mode='after')
    def telepathic_contact_report(self):
        if self.contact_type == "telepathic":
            if self.witness_count < 3:
                raise ValueError("Telepathic contact requires at least 3 witnesses")
        return self
    
    @model_validator(mode='after')
    def strong_signal(self):
        if self.signal_strength > 7:
            if self.message_received == None:
                raise ValueError("Strong signals (> 7.0) should include received messages")
            

def main() -> None:
    print("ALien Contact Log Validation")
    try:
        contact_log = AlienContact(
            contact_id = "AC_42",
            contact_type = ContactType.RADIO,
            location = "Area 51, Nevada",
            signal_strength = 8.5,
            duration_minutes = 45,
            witness_count = 5,
            message_received = "Greetings from Kevin's Reticuli"
        )
        print("=" * 40)
        print("Valid contact report:")
        print(f"ID: {contact_log.contact_id}")
        print(f"Type: {contact_log.contact_type}")
        print(f"Location: {contact_log.location}")
        print(f"Signal: {contact_log.signal_strength}/10")
        print(f"Duration: {contact_log.duration_minutes} minutes")
        print(f"Witnesses: {contact_log.witness_count}")
        print(f"Message: {contact_log.message_received}")
    except ValidationError:
        print("A ValidationError is caught")
