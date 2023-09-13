from fastapi import FastAPI, APIRouter

# from app.bom_auto.api.excel_upload import create_upload_file, create_download_file, download_bom
from view import insert_bug_info, show_all_bug_info, update_bug_info,update_bug_status
# 登录路由--不需要验证token
bug_router = APIRouter(
    responses={404: {"description": "Not found"}},
)


def bug_info_router(app: FastAPI):
    app.include_router(bug_router, tags=['BugTracking'])


bug_router.post("/bug_create", summary="BUG")(insert_bug_info)
bug_router.post("/bug_infos", summary="BUG")(show_all_bug_info)
bug_router.post("/bug_infos_update", summary="BUG")(update_bug_info)
bug_router.post("/bug_status_update", summary="BUG")(update_bug_status)
# bom_router.post('/uploadfile', summary=' 物料表上传本地 excel')(create_upload_file)
# bom_router.post("/new_bom", summary="下载BOM 新表")(download_bom)
