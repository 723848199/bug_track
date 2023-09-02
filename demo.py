from typing import Callable


def demo() -> Callable:
    print(111)
    return Callable


def demo01():
    def demo02(fun):
        print(fun())
        print('123')

    print('---')
    return demo02


demo01()(demo)
