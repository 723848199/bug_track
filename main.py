import uvicorn as uvicorn
from starlette.middleware.cors import CORSMiddleware

from core.events import startup, stopping
from core.server import server
from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union


class Item(BaseModel):
    name: str
    age: float
    is_TrueMan: Union[bool, None] = None


app = server.create_app()

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:8180/",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/", StaticFiles(directory=r"vue"), name="dist")

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
app.mount('/static', StaticFiles(directory=r"vue/static"), name="static")
templates = Jinja2Templates(directory=r"vue")
security = HTTPBasic()


@app.get("/a")
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/login", summary=" 登录")
def login(request: Request):
    # (credentials: HTTPBasicCredentials = security):
    # if credentials.username == "admin" and credentials.password == "password":
    # return templates.TemplateResponse("login.html", {"request": request})
    return templates.TemplateResponse(r"/html/1.html", {"request": request})
    # else:
    #     return {"Login": "Failed"}


@app.post("/demo", summary=" 登录")
def login(request: Request,username=Body()):
    print(username)
    return 23
    # return templates.TemplateResponse(r"/html/input.html", {"request": request})


# 事件监听
app.add_event_handler('startup', startup(app))
app.add_event_handler('shutdown', stopping(app))

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8180",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def demo():
    # user = await User.all()
    # print(user)
    return '123'

# 运行app
if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8180, reload=True)
