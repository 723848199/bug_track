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


# 运行app
if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8081, reload=True)
