from datetime import date
from pydantic import BaseModel


class HealthCheckRecordsSchema(BaseModel):
    id: int
    patient_id: int
    check_date: date
    status: str
    result_summary: str

    class Config:
        orm_mode = True
