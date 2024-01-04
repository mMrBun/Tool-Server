from datetime import date
from pydantic import BaseModel


class PatientsSchema(BaseModel):
    id: int
    name: str
    date_of_birth: date
    gender: str
    address: str
    phone_number: str

    class Config:
        orm_mode: True
