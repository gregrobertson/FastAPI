from pydantic import BaseModel
from typing import List, Optional, Union # to use OPTIONAL properties
from datetime import date # to use date field property
from queries.pool import pool

#Has nothing to do to with the database!!!!!!
#this class takes JSON and turns it into object

class Error(BaseModel):
    message: str
class VacationIn(BaseModel):
    # Unprocessable Entity Error: missing REQUIRED class properties
    name: str #REQUIRED
    from_date: date #REQUIRED
    to_date: date #REQUIRED
    thoughts: Optional[str] #NOT REQUIRED (  Optional [type OR class( for complex models)]  )

class VacationOut(BaseModel):
    # Unprocessable Entity Error: missing REQUIRED class properties
    id: int #REQUIRED
    name: str #REQUIRED
    from_date: date #REQUIRED
    to_date: date #REQUIRED
    thoughts: Optional[str] #NOT REQUIRED ( Optional[type OR class( for complex models)] )



class VacationRepository: #Repository Pattern
    def get_all(self) -> Union[Error, List[VacationOut]]:
        try:
            # Connect to the database
            with pool.connection() as conn:
                # Get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our SELECT statement
                    db.execute( #no second param needed, since we're getting all of the values
                        """
                        SELECT id, name, from_date, to_date, thoughts
                        FROM vacations
                        ORDER BY from_date;
                        """
                    )
                    result = []
                    for record in db:
                        vacation = VacationOut(
                            id=record[0],
                            name=record[1],
                            from_date=record[2],
                            to_date=record[3],
                            thoughts=record[4],
                        )
                        result.append(vacation)
                        return result
        except Exception as e:
            print(e)
            return {"message": "Could not get all vacations"}

    def create(self, vacation: VacationIn) -> VacationOut:
        try:
            # Connect to the database
            with pool.connection() as conn:
                # Get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our INSERT statement
                    result = db.execute( 
                        # %s are variable placeholders
                        """
                        INSERT INTO vacations
                            (name, from_date, to_date, thoughts)
                        VALUES 
                            (%s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [ # second param for getting specific values
                            vacation.name,
                            vacation.from_date, 
                            vacation.to_date, 
                            vacation.thoughts
                        ]
                    )

                    id = result.fetchone()[0]
                    # Return new data
                    old_data = vacation.dict() #turn vacation into a dictionary.
                    # return {"message":"error!"}
                    return VacationOut(id=id, **old_data) # **old_data returns all information from that instance of vacation
        except Exception:
            return {"message": "Create did not work"}

        
