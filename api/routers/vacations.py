from fastapi import APIRouter
from queiries.vacations import VacationIn

#used to define GET, POST, etc.
router = APIRouter()

#POST (endpoint)
@router.post("/vacations")
def create_vacation(vacation: VacationIn):
    print('vacation', vacation.name)
    return vacation