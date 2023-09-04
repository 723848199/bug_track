import uvicorn as uvicorn
from starlette.middleware.cors import CORSMiddleware

from core.events import startup, stopping
from core.server import server
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = server.create_app()

app.mount("/", StaticFiles(directory=r"E:\bug_track\vue"), name="dist")

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=r"E:\bug_track\vue")
security = HTTPBasic()
@app.get("/")
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
def login(credentials: HTTPBasicCredentials = security):
    if credentials.username == "admin" and credentials.password == "password":
        return templates.TemplateResponse("login.html")
    else:
        return {"Login": "Failed"}


# 事件监听
app.add_event_handler('startup', startup(app))
app.add_event_handler('shutdown', stopping(app))

async def demo():
    # user = await User.all()
    # print(user)
    return '123'

# 运行app
if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8080, reload=True)
