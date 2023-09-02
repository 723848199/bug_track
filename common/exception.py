from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from starlette.requests import Request


# from tools.utils.decorator import singleton


class HTTPException(Exception):
    """
    主动抛出异常返回
    """

    def __init__(self, code: int = 400, msg: str = '请求发生错误,请核对'):
        self.msg = msg
        self.code = code


class FastAPIException:
    """
    自定义异常捕获
    """

    def __init__(self, app: FastAPI):
        app.add_exception_handler(RequestValidationError, handler=self._request_validation_error)
        app.add_exception_handler(HTTPException, handler=self._register_exception)
        app.add_exception_handler(ResponseValidationError, handler=self._response_validation_error)

    @staticmethod
    async def _request_validation_error(request, exc: RequestValidationError):
        print(request)
        data = exc.errors()
        print(data)
        msg_list = []
        for details in data:
            par_type = details['loc'][0]
            par_name = details['loc'][1]
            print(details['msg'])
            match details['type']:
                case 'missing':
                    msg_list.append(f'{par_type} 中 {par_name} 参数不能为空')
                case 'string_too_short':
                    msg_list.append(f'{par_type} 中 {par_name} 长度不符合要求')
                case '-':
                    msg_list.append('未知错误,代核对')
        return JSONResponse(
            status_code=422,
            content=msg_list
        )

    @staticmethod
    async def _register_exception(request: Request, exc: HTTPException):
        print(request.url)
        return JSONResponse(
            status_code=exc.code,
            content=exc.msg
        )

    @staticmethod
    async def _response_validation_error(request, exc: ResponseValidationError):
        print(request)
        for i in exc.errors():
            print(i)
        return JSONResponse(
            status_code=422,
            content='验证错误'
        )
