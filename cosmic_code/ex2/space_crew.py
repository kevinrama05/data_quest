from pydantic import BaseModel, model_validator, Field, ValidationError
from enum import Enum
from datetime import datetime
from typing import List


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_id_validator(self) -> "SpaceMission":
        if self.mission_id[0] != "M":
            raise ValueError("Mission ID must start with 'M'")
        return self

    @model_validator(mode="after")
    def commander_or_captain_validation(self) -> "SpaceMission":
        for member in self.crew:
            if member.rank == Rank.CAPTAIN or member.rank == Rank.COMMANDER:
                return self
        raise ValueError("Must have at least one Commander or Captain")

    @model_validator(mode="after")
    def long_mission_validation(self) -> "SpaceMission":
        if self.duration_days > 365:
            experienced_members = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_members += 1
            if experienced_members >= len(self.crew) / 2:
                return self
            else:
                raise ValueError("Not enough experienced crew members")
        else:
            return self

    @model_validator(mode="after")
    def crew_members_validation(self) -> "SpaceMission":
        for member in self.crew:
            if member.is_active is False:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    """Demonstrate valid and invalid space mission crew validation."""
    print("Space Mission Crew Validation")
    print("=" * 41)

    # valid mission
    print("Valid mission created:")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 15, 9, 0, 0),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=45,
                    specialization="Mission Command",
                    years_experience=20,
                    is_active=True,
                ),
                CrewMember(
                    member_id="CM002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=32,
                    specialization="Navigation",
                    years_experience=8,
                    is_active=True,
                ),
                CrewMember(
                    member_id="CM003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=28,
                    specialization="Engineering",
                    years_experience=5,
                    is_active=True,
                ),
            ],
        )
        print(f"Mission:     {mission.mission_name}")
        print(f"ID:          {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration:    {mission.duration_days} days")
        print(f"Budget:      ${mission.budget_millions}M")
        print(f"Crew size:   {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"  - {member.name} ({member.rank.value})"
                f" - {member.specialization}"
            )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))

    print("=" * 41)

    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Failed Mission",
            destination="Venus",
            launch_date=datetime(2024, 7, 1, 9, 0, 0),
            duration_days=30,
            budget_millions=100.0,
            crew=[
                CrewMember(
                    member_id="CM004",
                    name="Bob Martinez",
                    rank=Rank.CADET,
                    age=22,
                    specialization="Science",
                    years_experience=1,
                    is_active=True,
                ),
                CrewMember(
                    member_id="CM005",
                    name="Carol White",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Medical",
                    years_experience=3,
                    is_active=True,
                ),
            ],
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
