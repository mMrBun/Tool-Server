from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        orm_mode = True
