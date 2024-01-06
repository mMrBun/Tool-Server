import datetime
from fastapi import Depends
from sqlalchemy.orm import Session
from db.curd.employment_inspection import query_employment_inspection
from db.database import get_db
from utils import BaseResponse
from utils.decorator import print_args


@print_args
def employment_inspection(db: Session = Depends(get_db)) -> BaseResponse:
    """
        查询普职检查
    """
    # 获取当前日期
    cur_time = datetime.datetime.now()
    # 计算今天是星期几（0 代表星期一，6 代表星期日）
    weekday = cur_time.weekday()
    # 计算距离下周一的天数（如果今天已经是周一，则返回 0；否则返回负数表示距离下周一还有多少天）
    days_until_next_monday = (0 - weekday) % 7
    # 计算下周一的日期
    next_monday = cur_time + datetime.timedelta(days=days_until_next_monday)
    # 计算下周五的日期
    next_friday = next_monday + datetime.timedelta(days=6)
    inspections = query_employment_inspection(next_monday, next_friday, db)
    # 定义一个星期字典
    week_dict = {
        0: "星期一",
        1: "星期二",
        2: "星期三",
        3: "星期四",
        4: "星期五",
        5: "星期六",
        6: "星期日"
    }
    # 根据星期将数据添加到相应的列表中
    message_str = ""
    result_dict = {day: 0 for day in week_dict.values()}
    for inspection in inspections:
        check_date, inspection_process, preparation = inspection
        week_day = check_date.weekday()
        result_dict[week_dict[week_day]] += 1
        if not message_str:
            message_str = f"检查流程：{inspection_process},注意事项：{preparation}"
    min_value = min(result_dict.values())
    min_keys = [key for key, value in result_dict.items() if value == min_value]
    return BaseResponse(code=200, msg="普职检查预约查询成功",
                        data=message_str + ",下周" + ",".join(min_keys) + "人最少")
