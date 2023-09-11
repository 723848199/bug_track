from typing import Callable


# 事件监听
def startup() -> Callable:
    async def app_start():

        print('启动完毕')

    return app_start


def stopping() -> Callable:
    async def stop_app() -> None:
        print('停止')

    return stop_app
