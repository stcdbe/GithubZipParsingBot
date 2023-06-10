import logging
from aiogram import executor, Dispatcher, Bot
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from bot.handlers.handlers import startmes, sendlogin, sendrepname, RepoNameStates, checkurl, righturl, wrongurl, echo
from bot.config import APITOKEN, REDISDB, REDISPORT, REDISHOST


def main() -> None:

    logging.basicConfig(level=logging.INFO)

    storage = RedisStorage2(host=REDISHOST, port=REDISPORT, db=REDISDB, pool_size=10, prefix='fsm')
    bot = Bot(APITOKEN)
    dp = Dispatcher(bot, storage=storage)

    dp.register_message_handler(startmes, commands=['start'])
    dp.register_message_handler(sendlogin, commands=['search'])
    dp.register_message_handler(sendrepname, state=RepoNameStates.login)
    dp.register_message_handler(checkurl, state=RepoNameStates.reponame)
    dp.register_callback_query_handler(righturl, lambda callback: callback.data == 'right')
    dp.register_callback_query_handler(wrongurl, lambda callback: callback.data == 'wrong')
    dp.register_message_handler(echo, lambda message: message == message)

    executor.start_polling(dispatcher=dp, skip_updates=True)
