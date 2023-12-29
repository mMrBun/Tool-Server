from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 配置信息
SQLALCHEMY_DATABASE_URL = "mysql://root:toolserver#7788@openwrt.mrbun.cn:9965/test"
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
