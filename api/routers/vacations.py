from fastapi import APIRouter
from queries.vacations import VacationIn

#used to define GET, POST, etc.
router = APIRouter()

#POST (endpoint)
@router.post("/vacations")
#from queries
def create_vacation(vacation: VacationIn):
    print('vacation', vacation)
    return vacation