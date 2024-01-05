from pydantic import BaseModel


class MedicationSchema(BaseModel):
    id: int
    medication_name: str
    dosage: str
    frequency: str

    class Config:
        orm_mode = True
