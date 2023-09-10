import hashlib
import uuid
from random import randrange


def code_number(length: int):
    """
    随机数字验证码
    :param length: 长度
    :return: str
    """
    code = ""
    for i in range(length):
        ch = chr(randrange(ord('0'), ord('9') + 1))
        code += ch

    return code


def random_str():
    """
    唯一随机字符串
    :return: str
    """
    only = hashlib.md5(str(uuid.uuid4()).encode(encoding='UTF-8')).hexdigest()
    return only
