from fastapi import FastAPI
from .routers import flights

app = FastAPI(title="Flight Monitoring API")

app.include_router(flights.router, prefix="/flights", tags=["flights"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Flight Monitoring API"}
