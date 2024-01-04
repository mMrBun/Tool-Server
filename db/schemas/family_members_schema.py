from pydantic import BaseModel


class FamilyMembersSchema(BaseModel):
    id : int
    patient_id : int
    name : str
    relation : str
    contact_number : str

    class Config:
        orm_mode = True
