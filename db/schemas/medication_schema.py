from pydantic import BaseModel


class MedicationSchema(BaseModel):
    id: int
    medication_name: str
    dosage: str
    frequency: str
    role: str
    taboo_information: str

    class Config:
        orm_mode = True
