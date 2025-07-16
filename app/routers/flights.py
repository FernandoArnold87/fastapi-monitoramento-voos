from typing import List
from fastapi import APIRouter, HTTPException
from ..models import Flight
from .. import database

router = APIRouter()

@router.get("/", response_model=List[Flight])
def list_flights():
    return database.flights_db

@router.get("/{flight_id}", response_model=Flight)
def get_flight(flight_id: int):
    for flight in database.flights_db:
        if flight.id == flight_id:
            return flight
    raise HTTPException(status_code=404, detail="Flight not found")

@router.post("/", response_model=Flight, status_code=201)
def create_flight(flight: Flight):
    if any(f.id == flight.id for f in database.flights_db):
        raise HTTPException(status_code=400, detail="Flight ID already exists")
    database.flights_db.append(flight)
    return flight

@router.put("/{flight_id}", response_model=Flight)
def update_flight(flight_id: int, flight: Flight):
    for idx, f in enumerate(database.flights_db):
        if f.id == flight_id:
            database.flights_db[idx] = flight
            return flight
    raise HTTPException(status_code=404, detail="Flight not found")

@router.delete("/{flight_id}", status_code=204)
def delete_flight(flight_id: int):
    for idx, f in enumerate(database.flights_db):
        if f.id == flight_id:
            database.flights_db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Flight not found")
