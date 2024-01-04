from sqlalchemy import Column, Integer, String, Date, Boolean
from db.database import Base


# 预约普职检查 场景五
class GeneralEmploymentInspection(Base):
    __tablename__ = "general_employment_inspection"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer)  # 病人id
    check_date = Column(Date)  # 检查时间
    inspection_process = Column(String)  # 检查流程
    preparation = Column(String)  # 准备事项
    status = Column(Boolean)  # 是否完成
