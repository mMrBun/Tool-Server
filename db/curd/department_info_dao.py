from sqlalchemy.orm import Session
from db.models.department_info import DepartmentInfoModel
from sqlalchemy.sql.expression import func


def query_department_info(db: Session, depart_name: str):
    """
    根据科室名查询科室信息
    """
    return db.query(DepartmentInfoModel).filter(DepartmentInfoModel.department_name == depart_name).first()


def query_department_by_symptom(db: Session, symptom: str):
    """
    根据科室名查询科室信息
    """
    return db.query(DepartmentInfoModel.department_name).filter(
        DepartmentInfoModel.corresponding_symptom.ilike(f"%{symptom}%")).all()
