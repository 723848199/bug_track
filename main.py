import uvicorn

from core.events import startup, stopping
from core.server import server


app = server.create_app()


# 事件监听
app.add_event_handler('startup', startup(app))
app.add_event_handler('shutdown', stopping(app))


async def demo():
    # user = await User.all()

    # print(user)
    return '123'


app.get('/')(demo)

# 运行app
if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8080, reload=True)
