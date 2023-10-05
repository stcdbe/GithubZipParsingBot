import pathlib

from aiofile import async_open
import aiohttp
from aiogram.dispatcher import FSMContext

from bot.requests.headers import getheaders


async def geturl(state: FSMContext) -> str:
    async with state.proxy() as data:
        login = data['login']
        reponame = data['reponame']
        url = f'https://github.com/{login}/{reponame}/'
    return url


async def getgitzip(state: FSMContext) -> bool:
    async with state.proxy() as data:
        login = data['login']
        reponame = data['reponame']
    async with aiohttp.ClientSession() as session:
        url = f'https://github.com/{login}/{reponame}/zipball/master/'
        async with session.get(url=url, headers=await getheaders()) as response:
            if response.status == 200:
                async with async_open(f'{reponame}.zip', 'wb') as file:
                    await file.write(await response.read())
                    return True
            return False


async def removefile(name: str) -> None:
    path = pathlib.Path(f'./{name}.zip')
    path.unlink()
