from sqlalchemy.orm import Session
from db.models.department_info import DepartmentInfoModel


def query_department_info(db: Session, depart_name: str):
    """
    根据科室名查询科室信息
    """
    return db.query(DepartmentInfoModel).filter(DepartmentInfoModel.department_name == depart_name).first()
