from datetime import datetime
from sqlalchemy import String, DateTime, Integer, Boolean, Text, BigInteger, Column
from sqlalchemy.orm import Mapped, mapped_column
# import enums

from db_engine import Base


class Staff_Information(Base):
    __tablename__ = "table_staff_information"
    id = Column(Integer, primary_key=True)
    worker_id = Column(String(20), comment="工号")
    worker_name = Column(String(20), comment="姓名")
    worker_post = Column(String(200), comment="职位")
    worker_apart = Column(String(200), comment="部门")
    reversed1 = Column(String(200), comment="reserved1")
    reversed2 = Column(String(200), comment="reserved2")
    reversed3 = Column(String(200), comment="reserved3")


class Bugs_Information(Base):
    __tablename__ = "table_bugs_information"
    id = Column(Integer, primary_key=True)
    worker_id = Column(String(20))
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, onupdate=datetime.now, default=datetime.now)
    bug_id = Column(String(50))
    bug_title = Column(String(200))
    bug_info = Column(Text)
    bug_details = Column(Text)
    bug_status = Column(Integer, comment="0:已关闭，1：进行中， -1：已删除")
    reversed1 = Column(String(200), comment="reserved1")
    reversed2 = Column(String(200), comment="reserved2")
    reversed3 = Column(String(200), comment="reserved3")
