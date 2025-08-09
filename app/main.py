from fastapi import FastAPI, BackgroundTasks
from .flights import get_flights, create_price_alert

app = FastAPI(title="Flight Monitor")

@app.get("/flights")
def flights(origin: str, destination: str, date: str):
    """Retrieve flight options from a third-party API."""
    return get_flights(origin, destination, date)

@app.post("/alerts")
def alerts(origin: str, destination: str, date: str, price: float, background_tasks: BackgroundTasks):
    """Create a price alert that checks periodically."""
    background_tasks.add_task(create_price_alert, origin, destination, date, price)
    return {"message": "Alert created"}
