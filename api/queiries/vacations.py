from optparse import Option
from pydantic import BaseModel
from typing import Optional

class VacationIn(BaseModel):
    name: str
    from_date: str
    to_date: str
    thoughts: Optional[str]
