from pydantic import BaseModel
from typing import Optional
from datetime import date

#Has nothing to do to with the database!!!!!!
#(FastAPI) takes JSON and turns it into object
class VacationIn(BaseModel):
    # Unprocessable Entity Error: 
    # missing REQUIRED class properties
    name: str
    from_date: date
    to_date: date
    #Not Required (put Optional['type'])
    thoughts: Optional[str]
