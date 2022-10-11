from optparse import Option
from pydantic import BaseModel
from typing import Optional

#Has nothing to do to with the database!!!!!!
#(FastAPI) takes JSON and turns it into object
class VacationIn(BaseModel):
    # Unprocessable Entity Error: 
    # missing REQUIRED class properties
    name: str
    from_date: str
    to_date: str
    #Not Required (put Optional['type'])
    thoughts: Optional[str]
