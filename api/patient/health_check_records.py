from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.schemas.health_check_records_schema import HealthCheckRecordsSchema
from utils import BaseResponse
from utils.decorator import print_args
from utils.token import verify_token
from db.models.health_check_records import HealthCheckRecords


@print_args
def get_latest_health_check_records(
        current_user: dict = Depends(verify_token),
        db: Session = Depends(get_db)
):
    """
    获取最新一次体检记录
    """
    if current_user.get("code") != 200:
        return BaseResponse(code=current_user.get("code"), msg=current_user.get("msg"), data=current_user.get("data"))
    patient = current_user.get("patient")
    latest_record = db.query(HealthCheckRecords).filter(HealthCheckRecords.patient_id == patient.id) \
        .order_by(HealthCheckRecords.check_date).first()
    records = HealthCheckRecordsSchema.from_orm(latest_record)
    return BaseResponse(code=200, msg="success", data=records)
