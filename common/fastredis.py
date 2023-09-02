import redis

from core import server


def get_redis():
    return redis.asyncio.Redis(connection_pool=server.redis_pool)
