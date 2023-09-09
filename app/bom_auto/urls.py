from fastapi import FastAPI, APIRouter

from app.bom_auto.api.excel_upload import create_upload_file, create_download_file, download_bom

# 登录路由--不需要验证token
bom_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

def bom_auto_router(app: FastAPI):
    app.include_router(bom_router, tags=['BOM物料表自动化实现接口'])


bom_router.post("/bom", summary="下载BOM 模板")(create_download_file)
bom_router.post('/uploadfile', summary=' 物料表上传本地 excel')(create_upload_file)
bom_router.post("/new_bom", summary="下载BOM 新表")(download_bom)


