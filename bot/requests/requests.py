import logging

from aiohttp import ClientSession
import aiofiles
from aiofiles.os import remove as aiofiles_os_remove


async def render_repo_url(url_data: dict[str, str]) -> str:
    username = url_data['username']
    repo_name = url_data['repo_name']
    url = f'https://github.com/{username}/{repo_name}/'
    return url


async def download_repo(url_data: dict[str, str]) -> str | None:
    username = url_data['username']
    repo_name = url_data['repo_name']
    download_url = f'https://github.com/{username}/{repo_name}/zipball/master/'

    async with ClientSession() as session:
        async with session.get(url=download_url) as res:
            if res.status == 200:
                zip_repo_name = repo_name + '.zip'
                async with aiofiles.open(zip_repo_name, 'wb') as file:
                    await file.write(await res.read())
                return zip_repo_name


async def del_repo(repo_name: str) -> None:
    try:
        await aiofiles_os_remove(repo_name)
    except FileNotFoundError:
        logging.warning('Attempt to delete a non-existent file: %s', repo_name)
