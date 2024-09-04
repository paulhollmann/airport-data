from typing import List, Literal, Optional
from pydantic import BaseModel, HttpUrl


class Link(BaseModel):
    category: Optional[Literal["Scenery", "Charts", "Briefing"]] = None
    name: str
    url: HttpUrl


class Airport(BaseModel):
    icao: str
    links: List[Link]


class AirportData(BaseModel):
    airports: List[Airport]
