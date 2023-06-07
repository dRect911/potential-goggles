from pydantic import BaseModel

class Vehicle(BaseModel):
    immatriculation: str
    owner: str
    category: str
    cotation: float

class Bill(BaseModel):
    immatriculations: list[str]
    cotation: float
    majoration: float
    total_amount: float
