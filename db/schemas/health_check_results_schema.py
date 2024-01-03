from pydantic import BaseModel


class HealthCheckResultsSchema(BaseModel):
    id = int
    record_id = int
    test_item = str
    result = str
    reference_range = str
    remark = str

    class Config:
        orm_mode: True
