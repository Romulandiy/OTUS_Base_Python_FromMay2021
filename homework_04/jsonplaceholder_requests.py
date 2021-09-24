"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

from dataclasses import dataclass

from aiohttp import ClientSession
from loguru import logger

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"



@dataclass
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service("ipify", "https://api.ipify.org/?format=json", "ip"),
    Service("ip-api", "http://ip-api.com/json", "query"),
]


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_ip(service: Service) -> str:
    logger.info("Fetch ip from {}", service.name)

    async with ClientSession() as session:
        result = await fetch_json(session, service.url)

    logger.info("Fetched json from {!r}: {}", service.name, result)

    return result.get(service.field)