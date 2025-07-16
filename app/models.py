from pydantic import BaseModel
from typing import Optional

class Flight(BaseModel):
    id: int
    origin: str
    destination: str
    status: Optional[str] = "scheduled"
