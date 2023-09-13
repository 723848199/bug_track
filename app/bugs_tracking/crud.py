from db_engine import session
from models import Staff_Information, Bugs_Information
from schemas import BugCreate, BugQueryID, BugDetail
from sqlalchemy.orm import Session
from datetime import datetime


#
# def insert_bug_information(db: Session, bug_info: BugCreate):
#     db_bug = Bugs_Information(**bug_info)
#     try:
#         db.add(db_bug)
#         db.commit()
#         db.refresh(db_bug)
#         return "success insert!"
#     except Exception as e:
#         return e
def get_all_bug_infos(db: Session):
    bug_info_list = []
    bug_infos = db.query(Bugs_Information).all()
    print(bug_infos)
    for items in bug_infos:
        bug_info_list.append({
            "id": items.id,
            "worker_id": items.worker_id,
            "create_time": items.create_time,
            "update_time": items.update_time,
            "bug_id": items.bug_id,
            "bug_title": items.bug_title,
            "bug_info": items.bug_info,
            "bug_details": items.bug_details
        })
    return bug_info_list


# def get_conditional_bug_infos(db:Session):
def insert_bug_information(bug_info: BugCreate, db: Session):
    create_time = datetime.now()
    # 根据时间创建单号
    bug_id = "B" + create_time.strftime("%Y%m%d%H%M%S%f")
    db_bug = Bugs_Information(**bug_info.dict(), bug_id=bug_id, create_time=create_time)
    try:
        db.add(db_bug)
        db.commit()
        db.refresh(db_bug)
        return "success insert!"
    except Exception as e:
        print("error")
        return e


def update_bug_info(bug_details: BugDetail, db: Session):
    # print(bug_details)
    # print(type(bug_details))
    print(bug_details)
    print(type(bug_details))
    bug_info = db.query(Bugs_Information).filter().all()
    print(bug_info)

    bug_info = db.query(Bugs_Information.id).filter(Bugs_Information.bug_id == bug_details.bug_id).all()
    print(bug_info)
    print(type(bug_info))

    # return bug_info


def update_bug_status(bug_id, status, db: Session):
    q = db.query(Bugs_Information).filter(Bugs_Information.bug_id == bug_id).first()
    if q and q.bug_status != status:
        try:
            db.query(Bugs_Information).filter(Bugs_Information.bug_id == bug_id).update({Bugs_Information.bug_status:status})
            db.commit()
            return "success"
        except Exception as e:
            db.rollback()
            return e
    else:
        return "No need to change"


def query_bug_info():
    pass

#
# db_bug = Bugs_Information(bug_title="bug_title",
#                           worker_id="worker_id")
#
# session.add(db_bug)
# session.commit()
