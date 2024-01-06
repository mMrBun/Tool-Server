from datetime import date

from pydantic import BaseModel


class DepartmentInfoSchema(BaseModel):
    department_id: int
    department_name: str
    department_phone: str
    location: str
    lead_physicians: str
    clinic_start_hours: str
    clinic_end_hours: str
    patient_guide: str

    class Config:
        orm_mode = True
