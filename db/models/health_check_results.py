from sqlalchemy import Column, Integer, String
from db.database import Base


class HealthCheckResults(Base):
    __tablename__ = "health_check_results"

    id = Column(Integer, primary_key=True, index=True)
    record_id = Column(Integer)
    test_item = Column(String)
    result = Column(String)
    reference_range = Column(String)
    remark = Column(String)
