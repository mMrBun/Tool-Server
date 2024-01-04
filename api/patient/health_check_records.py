from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc
from db.database import get_db
from db.schemas.health_check_records_schema import HealthCheckRecordsSchema
from utils import BaseResponse
from utils.decorator import print_args, verify_user_effective
from utils.token import verify_token
from db.models.health_check_records import HealthCheckRecords


@print_args
@verify_user_effective
def get_latest_health_check_record(
        current_user: dict = Depends(verify_token),
        db: Session = Depends(get_db)
):
    """
    获取最新一次体检记录
    """
    patient = current_user.get("patient")
    latest_record = db.query(HealthCheckRecords).filter(HealthCheckRecords.patient_id == patient.id) \
        .order_by(desc(HealthCheckRecords.check_date)).first()
    records = HealthCheckRecordsSchema.from_orm(latest_record)
    return BaseResponse(code=200, msg="success", data=records)
