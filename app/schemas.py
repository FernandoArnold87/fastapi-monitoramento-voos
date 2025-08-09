from pydantic import BaseModel

class Flight(BaseModel):
    flight_number: str
    origin: str
    destination: str
    date: str
    price: float

class AlertRequest(BaseModel):
    origin: str
    destination: str
    date: str
    price: float
