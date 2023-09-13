from fastapi import Body, Depends, Response, Request
from fastapi.security import OAuth2PasswordRequestForm

from app.bom_auto.bom_auto import bom_auto

from app.user.auth import verify_password, create_access_token, check_jwt_token
from app.user.models import User, Token

from fastapi import FastAPI, UploadFile, File
import openpyxl as op
import os
from fastapi.responses import FileResponse

from service import HTTPException, SMS
from service.utils.tools import code_number


async def create_upload_file(file: UploadFile = File(...)):
    '''
    客户可在此  上传BOM 操作表
    '''
    # contents = await file.read()
    wb = op.load_workbook(file.file)
    sheet1 = wb['原表']

    # 4.获取工作表名字列表
    sheet_names = wb.sheetnames
    print(sheet_names)
    return {"filename": file.filename, "contents": sheet_names}


async def create_download_file(filename: str):
    '''
     客户可在此 下载 BOM 物料表模板文件
    '''
    file_path = r"E:\bug_track\app\bom_auto\model_excel\bom_auto.xlsx"
    if os.path.exists(file_path):
        return FileResponse(file_path, filename='123.xlsx', media_type='xlsx')
    else:
        return {
            "msg": "沒有此文件"
        }


async def download_bom():
    '''
         客户可在此 下载 新BOM 表
    '''

    file_path = r"E:\bug_track\app\bom_auto\model_excel\bom_auto.xlsx"
    bom_auto(path=file_path)
    return FileResponse(file_path, filename='new_bom.xlsx', media_type='xlsx')


async def excel_upload(user: User = Depends(check_jwt_token)):
    pass


