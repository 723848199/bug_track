from typing import List
from schemas import BugCreate, BugDetail
from fastapi import FastAPI, HTTPException
from fastapi import Body, Depends, Response, Request
from sqlalchemy.orm import Session
from db_engine import session, engine
import crud


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


def show_all_bug_info(db: Session = Depends(get_db)):
    return crud.get_all_bug_infos(db)


def insert_bug_info(bug_info: BugCreate, db: Session = Depends(get_db)):
    # print(bug_info)
    result = crud.insert_bug_information(bug_info, db)
    # print(result)
    return result


def update_bug_info(bug_info: BugDetail, db: Session = Depends(get_db)):
    crud.update_bug_info(bug_info, db)
    # print(result)
    # return result


def update_bug_status(bug_id:str, status:str, db:Session = Depends(get_db)):
    result = crud.update_bug_status(bug_id, status, db)
    return result