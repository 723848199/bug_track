# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from core.config import settings

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy import ForeignKey

from datetime import datetime

MYSQL_SERVER: str = "127.0.0.1"
MYSQL_PORT: str = "3306"
MYSQL_USER: str = "root"
MYSQL_PASSWORD: str = "123456"
MYSQL_DB: str = "test"
MYSQL_CHARSET: str = "utf8mb4"

# SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
# General engine for SQL connection to the backend database
DB_DIR = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}?charset={MYSQL_CHARSET}"
engine = create_engine(DB_DIR)
Base = declarative_base()
session = sessionmaker(bind=engine)

#
# class Staff_Information(Base):
#     __tablename__ = "table_staff_information"
#     id = Column(Integer, primary_key=True)
#     worker_id = Column(String(20), comment="工号")
#     worker_name = Column(String(20), comment="姓名")
#     worker_post = Column(String(200), comment="职位")
#     worker_apart = Column(String(200), comment="部门")
#     reversed1 = Column(String(200), comment="reserved1")
#     reversed2 = Column(String(200), comment="reserved2")
#     reversed3 = Column(String(200), comment="reserved3")
#
#
# class Bugs_Information(Base):
#     __tablename__ = "table_bugs_information"
#     id = Column(Integer, primary_key=True)
#     worker_id = Column(String(20))
#     create_time = Column(DateTime, default=datetime.now)
#     update_time = Column(DateTime, onupdate=datetime.now, default=datetime.now)
#     bug_id = Column(String(50))
#     bug_title = Column(String(200))
#     bug_info = Column(Text)
#     bug_details = Column(Text)
#     bug_status = Column(Integer, comment="0:已关闭，1：进行中")
#     reversed1 = Column(String(200), comment="reserved1")
#     reversed2 = Column(String(200), comment="reserved2")
#     reversed3 = Column(String(200), comment="reserved3")


# class Bugs_Information_Modified(Base):

# t = Test_Table(price=10)
# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
