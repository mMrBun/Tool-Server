from fastapi import Depends
from sqlalchemy.orm import Session

from db.curd.vaccination_dao import get_vaccinations_for_patient
from db.database import get_db
from db.models.patients import Patients
from utils import BaseResponse
from utils.token import verify_token


def get_vaccination_record(current_user: dict = Depends(verify_token), db: Session = Depends(get_db)) -> BaseResponse:
    """
    查询患者疫苗接种记录
    """
    patients = current_user.get("patient")
    patient_id = patients.id
    vacc_list = get_vaccinations_for_patient(db, patient_id)
    if len(vacc_list) != 0:
        data = [{
            "vaccine_name": v.vaccine_name,
            "vaccination_date": v.vaccination_date,
            "vaccination_provider": v.vaccination_provider,
            "vaccination_location": v.vaccination_location
        } for v in vacc_list]
        return BaseResponse(code=200, msg="查询成功", data=data)
    return BaseResponse(code=200, msg="查询成功", data="暂无接种记录")
