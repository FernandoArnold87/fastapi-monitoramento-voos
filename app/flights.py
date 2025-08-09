import httpx
import asyncio
from typing import List

# Placeholder third-party API URL (this would normally require an API key)
API_URL = "https://api.example.com/flights"

async def fetch_flights(origin: str, destination: str, date: str) -> List[dict]:
    """Fetch flights from a third-party provider."""
    params = {"from": origin, "to": destination, "date": date}
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL, params=params)
        response.raise_for_status()
        return response.json()

# In a real application this would check prices on a schedule and send notifications
async def monitor_price(origin: str, destination: str, date: str, price: float):
    flights = await fetch_flights(origin, destination, date)
    for flight in flights:
        if flight.get("price") <= price:
            # Here we would notify the user (email, SMS, etc.)
            print(f"Price alert! {flight}")

# Wrappers for FastAPI synchronous endpoints

def get_flights(origin: str, destination: str, date: str):
    """Synchronous wrapper around ``fetch_flights`` for FastAPI."""
    return asyncio.run(fetch_flights(origin, destination, date))

def create_price_alert(origin: str, destination: str, date: str, price: float):
    """Synchronous wrapper to start price monitoring."""
    return asyncio.run(monitor_price(origin, destination, date, price))
