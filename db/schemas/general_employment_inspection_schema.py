from datetime import date
from pydantic import BaseModel


class GeneralEmploymentInspectionSchema(BaseModel):
    id: int
    patient_id: int
    check_date: date
    inspection_process: str
    preparation: str
    status: bool

    class Config:
        orm_mode: True
