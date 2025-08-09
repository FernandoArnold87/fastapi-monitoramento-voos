# Flight Monitoring with FastAPI

This repository contains a simple FastAPI application that demonstrates how to monitor flights and create price alerts.

## Setup

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

- `GET /flights?origin=FROM&destination=TO&date=YYYY-MM-DD` – search for flights.
- `POST /alerts?origin=FROM&destination=TO&date=YYYY-MM-DD&price=VALUE` – create a price alert.

This example uses a placeholder flight API and prints alerts to the console. Integrate a real flight API and notification service for production use.
