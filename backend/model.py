from pydantic import BaseModel
from typing import List

class Odds(BaseModel):
    one: float
    x: float
    two: float

class Match(BaseModel):
    teams: str
    odds: Odds

class Matches(BaseModel):
    matches: List[Match]