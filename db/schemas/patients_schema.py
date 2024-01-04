from datetime import date
from pydantic import BaseModel, model_serializer
from pydantic_core.core_schema import SerializationInfo


class PatientsSchema(BaseModel):
    id: int
    name: str
    date_of_birth: date
    gender: str
    address: str
    phone_number: str

    class Config:
        orm_mode: True

    # @model_serializer
    # def ser_model(self, info: SerializationInfo):
    #     return {'id': f' {self.id}',
    #             'name': f'{self.name}',
    #             'date': f'{self.date_of_birth}',
    #             'gender': f'{self.gender}',
    #             'address': f'{self.address}',
    #             'phone_number': f'{self.phone_number}'}
