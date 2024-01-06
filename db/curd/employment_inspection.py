import datetime

from sqlalchemy import and_
from sqlalchemy.orm import Session
from db.models.general_employment_inspection import GeneralEmploymentInspection


def query_employment_inspection(next_monday, next_friday, db: Session):
    inspections = db.query(GeneralEmploymentInspection.check_date, GeneralEmploymentInspection.inspection_process,
                           GeneralEmploymentInspection.preparation).filter(
        and_(GeneralEmploymentInspection.check_date >= next_monday.date(),
             GeneralEmploymentInspection.check_date <= next_friday.date()),
    )
    return inspections
