from datetime import datetime, date

from pydantic import BaseModel


class PatientsMedicationRecordsSchema(BaseModel):
    id: int
    patients_id: int
    medication_id: int
    create_time: date

    class Config:
        orm_mode: True
