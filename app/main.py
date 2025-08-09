from typing import List

import httpx
from fastapi import BackgroundTasks, FastAPI, HTTPException

from .flights import fetch_flights, monitor_price
from .schemas import AlertRequest, Flight

app = FastAPI(title="Flight Monitor")

@app.get("/flights", response_model=List[Flight])
async def flights(origin: str, destination: str, date: str):
    """Retrieve flight options from a third-party API."""
    try:
        return await fetch_flights(origin, destination, date)
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=502, detail=str(exc))

@app.post("/alerts")
async def alerts(alert: AlertRequest, background_tasks: BackgroundTasks):
    """Create a price alert that checks periodically."""
    background_tasks.add_task(
        monitor_price, alert.origin, alert.destination, alert.date, alert.price
    )
    return {"message": "Alert created"}
