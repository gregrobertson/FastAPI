from pydantic import BaseModel
from typing import Optional # to use OPTIONAL properties
from datetime import date # to use date field property
from queries.pool import pool

#Has nothing to do to with the database!!!!!!
#this class takes JSON and turns it into object
class VacationIn(BaseModel):
    # Unprocessable Entity Error: missing REQUIRED class properties
    name: str #REQUIRED
    from_date: date #REQUIRED
    to_date: date #REQUIRED
    thoughts: Optional[str] #NOT REQUIRED ( Optional[type OR class( for complex models)] )


class VacationRepository: #Repository Pattern
    def create(vacation: VacationIn):
        # Connect to the database
        with pool.connection() as conn:
            # Get a cursor (something to run SQL with)
            with conn.cursor() as db:
                # Run our INSERT statement
                result = db.execute( # %s are variable placeholders
                    """
                    INSERT INTO vacations
                        (name, from_date, to_date, thoughts)
                    VALUES
                        (%s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [
                        vacation.name,
                        vacation.from_date, 
                        vacation.to_date, 
                        vacation.thoughts
                    ]
                )
                print(result)
                # Return new data
        
