## 框架

1. FastAPI
2. pg数据库
3. redis

## 实现功能

jwt token认证

阿里云短信服务接入

### 用户

注册,登录认证,查看信息

### 项目结构

** 项目结构采用基于应用的结构 **

* `app`  --项目模块目录
    * `user` --用户模块
        * `api` --api接口
        * `auth.py` --用户认证相关
        * `models.py` --子模块模型
        * `urls` --子模块路由
        * `schemas.py` --子模块序列化模型
    * `...目录` --其他模块
    * `models.py` --公共模型
    * `routers.py` --总路由管理
* `service` --项目服务功能
    * `utils` -- 公共方法目录
    * `events.py` --事件监听文件
    * `exception.py` --异常捕获
    * `server` --项目服务
    * `sms_service` --阿里云短信服务
* `static` --静态资源目录
* `test` --单元测试目录
* `main.py` --项目入口
* `settings.py` --项目配置文件
* `.env` --环境变量(本地文件,不上传代码仓)
* `.gitginre` --git管理排除文件

```shell
pip install "fastapi[all]"
pip install python-jose[cryptography]
pip install passlib[bcrypt]
pip install tortoise-orm
pip install tortoise-orm[asyncpg]
pip install alibabacloud_ecs20140526==3.0.7
pip install alibabacloud_dysmsapi20170525==2.0.23
pip install redis
```