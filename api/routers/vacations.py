from fastapi import APIRouter, Depends, Response
from typing import Union, List
from queries.vacations import Error, VacationIn, VacationRepository, VacationOut

#used to define GET, POST, etc.
router = APIRouter()

#POST (endpoint , what we want to show)
@router.post("/vacations", response_model=Union[VacationOut, Error])
#from queries
def create_vacation(
    vacation: VacationIn,
    response: Response,
    repo: VacationRepository = Depends()
):
    response.status_code = 400
    return repo.create(vacation)

@router.get("/vacations", response_model=Union[Error, List[VacationOut]])
def get_all(
    repo: VacationRepository = Depends(),
):
    return repo.get_all()