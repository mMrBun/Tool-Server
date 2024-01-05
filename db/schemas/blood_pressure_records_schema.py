from datetime import date

from pydantic import BaseModel


class BloodPressureRecordsSchema(BaseModel):
    id: int
    patient_id: int
    systolic_pressure: int
    diastolic_pressure: int
    create_time: date

    class Config:
        orm_mode = True
