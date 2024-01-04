from fastapi import Depends
from requests import Session

from db.database import get_db
from utils.token import verify_token
from db.models.health_check_records import HealthCheckRecords
from db.models.health_check_results import HealthCheckResults


def get_health_check_records(
        current_user: dict = Depends(verify_token),
        db: Session = Depends(get_db)
):
    ...
    print(current_user.values())
    print(db)
