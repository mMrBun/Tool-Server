from typing import Any, List
import pydantic
from pydantic import BaseModel


class BaseResponse(BaseModel):
    code: int = pydantic.Field(200, description="API status code")
    msg: str = pydantic.Field("success", description="API status message")
    data: Any = pydantic.Field(None, description="API data")

    class Config:
        schema_extra = {
            "example": {
                "code": 200,
                "msg": "success",
            }
        }


class TokenResponse(BaseModel):
    access_token: str = pydantic.Field(None, description="token str")
    token_type: str = pydantic.Field("bearer", description="token type")
