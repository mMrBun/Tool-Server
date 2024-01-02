from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from conf.pyconfig.config_read import configRead

# 配置信息
database_config = configRead.get_config("database.yaml")
assert database_config, "未加载到数据库配置"
SQLALCHEMY_DATABASE_URL = f"{database_config['database']['DB_TYPE']}://{database_config['database']['USER']}:{database_config['database']['PASSWORD']}@{database_config['database']['HOST']}:{database_config['database']['PORT']}/{database_config['database']['DATABASE']}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
