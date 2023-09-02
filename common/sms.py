from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_util import models as util_models
from pydantic import BaseModel

from core import setting
from common.exception import HTTPException


class SMSAaLiInfo(BaseModel):
    sign_name: str
    template_code: str


# 短信模版信息,需在阿里云控制中心申请
login_code = SMSAaLiInfo(sign_name='阿里云短信测试', template_code='SMS_154950909')


class SMS:
    __access_key_id = setting.ALIBABA_CLOUD_ACCESS_KEY_ID
    __access_key_secret = setting.ALIBABA_CLOUD_ACCESS_KEY_SECRET

    @classmethod
    def __create_client(cls) -> Dysmsapi20170525Client:
        """
        使用AK&SK初始化账号Client
        :return: 
        """""
        config = open_api_models.Config(
            access_key_id=cls.__access_key_id,
            access_key_secret=cls.__access_key_secret
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Dysmsapi
        config.endpoint = f'dysmsapi.aliyuncs.com'
        return Dysmsapi20170525Client(config)

    @classmethod
    async def send_code(cls, phone, code, code_type=1):
        """
        
        :param phone:   手机号
        :param code:    验证码
        :param code_type:   验证码类型--对应使用的模版 
        :return: 
        """""
        client = cls.__create_client()
        match code_type:
            case 1:
                data_type = login_code
            case _:
                raise HTTPException(msg=f'类型错误,请核对')
        # send_sms_request = dysmsapi_20170525_models.SendSmsRequest(sign_name=data_type.sign_name,
        #                                                            template_code=data_type.template_code,
        #                                                            phone_numbers=str(phone),
        #                                                            template_param=str({'code': str(code)}))
        # runtime = util_models.RuntimeOptions()
        # try:
        #     ret = await client.send_sms_with_options_async(send_sms_request, runtime)
        # except Exception:
        #     raise HTTPException(msg='短信发送失败')
        # if ret.status_code != 200 or ret.body.message != 'OK':
        #     raise HTTPException(msg=f'短信发送失败---{ret.body.message}')
