from typing import List, Union
from pydantic import BaseModel


class Stand(BaseModel):
    icao: str
    stand: str
    lat: Union[float, List[float]]
    lon: Union[float, List[float]]
