from fastapi import FastAPI, APIRouter

from app.bom_auto.api.excel_upload import  create_upload_file
from app.user.urls import user_routers

# 登录路由--不需要验证token
bom_auto = APIRouter(
    responses={404: {"description": "Not found"}},
)

def bom_auto_router(app: FastAPI):
    app.include_router(bom_auto, tags=['BOM 物料表上传'])

bom_auto.post('/uploadfile', summary=' 物料表上传本地 excel')(create_upload_file)


