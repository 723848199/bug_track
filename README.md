## 框架

1. fastapi
2. pg数据库
3. redis

## 实现功能

jwt token认证

阿里云短信服务接入

### 用户

注册,登录认证,查看信息

### 项目结构

* `app`  --项目源目录
    * `bom_auto` --bom_excel模块
        * `api` --bom_excel api接口
        * `models.py` --子模块模型
        * `urls` --子模块路由
        * `schemas.py` --子模块序列化模型
    * `user` --用户模块
        * `api` --用户模块 api接口
        * `auth.py` --认证相关
        * `models.py` --子模块模型
        * `urls` --子模块路由
        * `schemas.py` --子模块序列化模型
    * `...目录` --其他模块
    * `models.py` --公共模型
    * `urls.py` --总路由管理
    * `schemas.py` --总序列化模型
* `service` --公共函数目录
* `notebook` --笔记目录,和项目无关
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

## 教程文档

### FastAPI

python web 框架
官网地址:https://fastapi.tiangolo.com

> python web 框架经常用的 主要是 django Flask 与 FastAPI ,
> django大而全,什么都有,4.0 之后也开始支持异步,上手简单,官网教程全, 什么都有,太大,太重,性能方面不是很好,
> Flask 基于 WSGI 的 轻量的 web 框架,自定义功能强.(WSGI 是为 Python 语言定义的 Web 服务器和 Web
> 应用程序或框架之间的一种简单而通用的接口。)
> FastAPI 基于 ASGI 的异步 web 框架,性能强,自定义功能强(ASGI 是异步网关协议接口，一个介于网络协议服务和 Python
> 应用之间的标准接口，能够处理多种通用的协议类型，包括 HTTP、HTTP2 和 WebSocket。)

### Tortoise orm

python orm 框架 (数据库中间件)
官网地址: https://tortoise.github.io/
> python 常用的 orm 框架是 SWLAlchemy orm, tortoise orm 是受 django 启发的异步 orm 框架,用法基本与 django 的一直,可以直接看参考
> django 文档.
> SWLAlchemy 语法与 SQL 语法类似,需要自己实现 crud ,对异步支持不是很好,学习曲线重.
> tortoise orm 为异步创建的 orm 框架,使用方式比SWLAlchemy简单,性能强,

### postgresql

数据库
官网地址:https://www.postgresql.org/
> MySQL与PostGreSQL的区别

> 一.PostgreSQL相对于MySQL的优势
> 1. 在SQL的标准实现上要比MySQL完善，而且功能实现比较严谨；
> 2. 存储过程的功能支持要比MySQL好，具备本地缓存执行计划的能力；
> 3. 对表连接支持较完整，优化器的功能较完整，支持的索引类型很多，复杂查询能力较强；
> 4. PG主表采用堆表存放，MySQL采用索引组织表，能够支持比MySQL更大的数据量。
> 5. PG的主备复制属于物理复制，相对于MySQL基于binlog的逻辑复制，数据的一致性更加可靠，复制性能更高，对主机性能的影响也更小。
> 6. MySQL的存储引擎插件化机制，存在锁机制复杂影响并发的问题，而PG不存在。

> 二、MySQL相对于PG的优势：
> 1. innodb的基于回滚段实现的MVCC机制，相对PG新老数据一起存放的基于XID的MVCC机制，是占优的。因此MySQL的速度是高于PG的；
> 2. MySQL采用索引组织表，这种存储方式非常适合基于主键匹配的查询、删改操作，但是对表结构设计存在约束；
> 3. MySQL的优化器较简单，系统表、运算符、数据类型的实现都很精简，非常适合简单的查询操作；
> 4. MySQL分区表的实现要优于PG的基于继承表的分区实现，主要体现在分区个数达到上千上万后的处理性能差异较大。

> 总结：
>
PG具备更高的可靠性，对数据一致性完整性的支持高于MySQL，因此PG更加适合严格的企业应用场景（比如金融、电信、ERP、CRM）；而MySQL查询速度较快，更加适合业务逻辑相对简单、数据可靠性要求较低的互联网场景（比如google、facebook、alibaba）。

### redis

REmote DIctionary Server(Redis) 是一个由 Salvatore Sanfilippo 写的 key-value 存储系统，是跨平台的非关系型数据库。

本项目中主要使用 redis 记录验证码,数据缓存等非持久化数据