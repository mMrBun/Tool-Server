from datetime import date
from pydantic import BaseModel


class MedicationRecordsSchema(BaseModel):
    id: int
    patient_id: int
    medication_name: str
    prescribed_date: date
    dosage: str
    frequency: str
    is_delete: str

    class Config:
        orm_mode = True
