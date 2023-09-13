from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class Bug_info(BaseModel):
    worker_id: str


class BugCreate(BaseModel):
    worker_id: str
    bug_title: str
    bug_info: Optional[Bug_info]
    bug_details: str
    bug_status: int = 1


class BugQueryID(BaseModel):
    id: int


class BugDetail(BaseModel):
    worker_id: Optional[str]
    update_time: None
    bug_id: str = "B20230913093954446943"
    bug_title: Optional[str]
    bug_info: Optional[Bug_info]
    bug_details: Optional[str]
    bug_status: Optional[int]


