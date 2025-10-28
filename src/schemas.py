from enum import Enum
from pydantic import BaseModel

class Options(Enum):
    DRAW = 'draw'
    CSV = 'csv'
    DEBUG = 'debug'
    RETURN_RESULTS = 'return_results'


class StreamData(BaseModel):
    CP: float
    TSUPPLY: float
    TTARGET: float