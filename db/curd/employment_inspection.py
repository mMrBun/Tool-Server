import datetime

from sqlalchemy import and_
from sqlalchemy.orm import Session
from db.models.general_employment_inspection import GeneralEmploymentInspection


def query_employment_inspection(db: Session):
    # 获取当前日期
    cur_time = datetime.datetime.now()
    # 计算今天是星期几（0 代表星期一，6 代表星期日）
    weekday = cur_time.weekday()
    # 计算距离下周一的天数（如果今天已经是周一，则返回 0；否则返回负数表示距离下周一还有多少天）
    days_until_next_monday = (0 - weekday) % 7
    # 计算下周一的日期
    next_monday = cur_time + datetime.timedelta(days=days_until_next_monday)
    # 计算下周五的日期
    next_friday = next_monday + datetime.timedelta(days=4)
    inspections = db.query(GeneralEmploymentInspection.check_date,GeneralEmploymentInspection.inspection_process,GeneralEmploymentInspection.preparation).filter(
        and_(GeneralEmploymentInspection.check_date >= next_monday.date(),
             GeneralEmploymentInspection.check_date <= next_friday.date()),
    )
    return inspections
