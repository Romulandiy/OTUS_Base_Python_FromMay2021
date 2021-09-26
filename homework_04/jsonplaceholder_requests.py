"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
from dataclasses import dataclass

from aiohttp import ClientSession
from loguru import logger


@dataclass
class Service:
    name: str
    url: str
    fields: list


USERS_DATA_URL = 'https://jsonplaceholder.typicode.com/users'
POSTS_DATA_URL = 'https://jsonplaceholder.typicode.com/posts'

# SERVICES = [USERS_DATA_URL, POSTS_DATA_URL]
SERVICES = [
    Service('json_users', USERS_DATA_URL, ['name', 'username', 'email']),
    Service('json_posts', POSTS_DATA_URL, ['user_id', 'title', 'body']),
]


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_fields(service: SERVICES):
    logger.info("Fetch from {}", service.name)

    async with ClientSession() as session:
        result = await fetch_json(session, service.url)

    logger.info("Fetched json {}", result)

    return result


async def async_main():
    for i in SERVICES:
        await fetch_fields(i)


def main():
    asyncio.run(async_main())


if __name__ == '__main__':
    main()

# @dataclass
# class Service:
#     name: str
#     url: str
#     field: str
#
#
# SERVICES = [
#     Service("ipify", "https://api.ipify.org/?format=json", "ip"),
#     Service("ip-api", "http://ip-api.com/json", "query"),
# ]
#
#
# async def fetch_json(session: ClientSession, url: str) -> dict:
#     async with session.get(url) as response:
#         return await response.json()
#
#
# async def fetch_ip(service: Service) -> str:
#     logger.info("Fetch ip from {}", service.name)
#
#     async with ClientSession() as session:
#         result = await fetch_json(session, service.url)
#
#     logger.info("Fetched json from {!r}: {}", service.name, result)
#
#     return result.get(service.field)
#
#
# async def async_main():
#     for service in SERVICES:
#         await fetch_ip(service)
#
#
# def main():
#     asyncio.run(async_main())
#
#
# if __name__ == '__main__':
#     main()
