import uvicorn

from app import router
from service import server
from service.events import startup, stopping

app = server.create_app()

# # 事件监听
app.add_event_handler('startup', startup())
app.add_event_handler('shutdown', stopping())

# 链接 redis 数据库
app.state.check = server.redis_link(0)  # 验证码缓存
app.state.cache = server.redis_link(1)  # 数据缓存

# 异常拦截
server.exception()
# 链接数据库
server.db_link()
# 跨域设置
server.cors()

# 挂接子路由
router(app=app)

# app.mount("/", StaticFiles(directory=r"vue"), name="dist")
# app.mount('/static', StaticFiles(directory=r"vue/static"), name="static")
# templates = Jinja2Templates(directory=r"vue")
# security = HTTPBasic()
#
# @app.get("/")
# def login_form(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})
#
# @app.get("/login", summary=" 登录")
# def login(request: Request):
#     # (credentials: HTTPBasicCredentials = security):
#     # if credentials.username == "admin" and credentials.password == "password":
#     # return templates.TemplateResponse("login.html", {"request": request})
#     return templates.TemplateResponse(r"/html/1.html", {"request": request})
#     # else:
#     #     return {"Login": "Failed"}
#
#
# @app.post("/demo", summary=" 登录")
# def login(request: Request,username=Body()):
#     print(username)
#     return 23
#     # return templates.TemplateResponse(r"/html/input.html", {"request": request})

# 运行app
if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8080, reload=True)
