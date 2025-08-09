import asyncio
from typing import List

import httpx

from .schemas import Flight

# Placeholder third-party API URL (this would normally require an API key)
API_URL = "https://api.example.com/flights"


async def fetch_flights(origin: str, destination: str, date: str) -> List[Flight]:
    """Fetch flights from a third-party provider."""
    params = {"from": origin, "to": destination, "date": date}
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL, params=params)
        response.raise_for_status()
        flights = response.json()
    return [Flight(**f) for f in flights]


async def monitor_price(
    origin: str,
    destination: str,
    date: str,
    price: float,
    interval: int = 60,
):
    """Periodically check flight prices and report when below threshold."""
    while True:
        flights = await fetch_flights(origin, destination, date)
        for flight in flights:
            if flight.price <= price:
                # Here we would notify the user (email, SMS, etc.)
                print(f"Price alert! {flight}")
        await asyncio.sleep(interval)
