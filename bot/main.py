import logging

from aiogram import Dispatcher, Bot
from aiogram.methods import DeleteWebhook
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from bot.config import settings, REDIS_URL
from bot.handlers.handlers import main_router


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    aioredis = Redis.from_url(url=REDIS_URL)
    storage = RedisStorage(redis=aioredis)
    bot = Bot(token=settings.BOT_API_TOKEN)
    dp = Dispatcher(storage=storage)

    await bot(DeleteWebhook(drop_pending_updates=True))

    dp.include_router(main_router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
