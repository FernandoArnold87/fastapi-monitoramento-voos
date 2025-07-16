from typing import List
from .models import Flight

# In-memory data store
flights_db: List[Flight] = [
    Flight(id=1, origin="JFK", destination="LAX", status="scheduled"),
    Flight(id=2, origin="LHR", destination="DXB", status="delayed"),
]
