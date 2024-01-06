import threading
from db.curd.department_info_dao import query_department_info, query_department_by_symptom
from utils.decorator import *
from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from utils.token import verify_token
from db.schemas.department_info_schema import DepartmentInfoSchema

department_counters = {}


@print_args
# @verify_user_effective
def get_department_info_by_name(name: str, db: Session = Depends(get_db)) -> BaseResponse:
    """
    根据科室名称获取科室信息
    此API接口不需要认证，可随意访问
    """
    info = query_department_info(db, name)
    if info is None:
        return BaseResponse(data="暂无此科室信息")
    department_info = DepartmentInfoSchema.from_orm(info)
    return BaseResponse(data=department_info)


@print_args
@verify_user_effective
def patients_registration(name: str, current_user: dict = Depends(verify_token),
                          db: Session = Depends(get_db)) -> BaseResponse:
    """
    患者根据科室名称挂号
    """
    lock = None
    info = query_department_info(db, name)
    patient = current_user.get("patient")
    if info is None:
        return BaseResponse(data="暂无此科室信息")
    if lock is None:
        lock = threading.Lock()

    with lock:
        # 检查科室是否已经在计数器字典中
        if name not in department_counters:
            # 如果没有，初始化该科室的挂号号码为1
            department_counters[name] = 1
        else:
            # 如果已经存在，将该科室的挂号号码增加1
            department_counters[name] += 1
        # time.sleep(3)
        registration_number = department_counters[name]
        department_info = DepartmentInfoSchema.from_orm(info)
        data = {"number:": registration_number, "patient_name": patient.nickname, "department_info": department_info}
        return BaseResponse(data=data)


@print_args
def department_consultation(symptom: str, db: Session = Depends(get_db)) -> BaseResponse:
    """
        相关症状对应相关科室
    """
    department_names = query_department_by_symptom(db, symptom)

    return BaseResponse(data=[department[0] for department in department_names])
