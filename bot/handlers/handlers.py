from aiofile import async_open
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from bot.keyboards.keyboards import checkkb
from bot.requests.requests import geturl, getgitzip, removefile
from bot.statesgroup.statesgroup import RepoNameStates


async def startmes(message: types.Message) -> None:
    await message.answer(text='Hi\nI\'m bot which can get Github repository in ZIP format.'
                              '\nFor finding repository click /search ')


async def sendlogin(message: types.Message) -> None:
    await message.answer(text='Send Github repository owner login.')
    await RepoNameStates.login.set()


async def sendrepname(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['login'] = message.text
    await RepoNameStates.next()
    await message.answer(text='Send repository title.')


async def checkurl(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['reponame'] = message.text
    await message.answer(text=await geturl(state))
    await getgitzip(state)
    await message.answer(text='Do you want to download this repository?', reply_markup=await checkkb())
    await RepoNameStates.next()


async def righturl(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await callback.message.delete()
    gitzip = await getgitzip(state)
    if not gitzip:
        await callback.message.answer(text='Download error.'
                                           '\nCheck correctness of the selected repository'
                                           ' and try again. \n/search')
    else:
        async with state.proxy() as data:
            reponame = data['reponame']
            async with async_open(f'{reponame}.zip', 'rb') as file:
                await callback.message.answer_document(document=file,
                                                        caption=f'{reponame}.zip',
                                                        disable_content_type_detection=True)
            await removefile(name=reponame)
            await callback.message.answer(text='To get one more repository click /search')
    await state.finish()


async def wrongurl(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer(text='If you want to try again just click /search')
    await state.finish()


async def echo(message: types.Message) -> None:
    await message.answer(text='Unknown command.')
