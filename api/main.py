from fastapi import FastAPI
from routers import vacations

#create app
app = FastAPI()
#include all the routers for vacation endpoint
app.include_router(vacations.router)

