from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str
    username: str

    class Config:
        orm_mode = True
