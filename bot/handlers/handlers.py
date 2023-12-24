import logging

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, FSInputFile, ErrorEvent
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from bot.keyboards.keyboards import get_url_confirm_kb
from bot.requests.requests import del_repo, render_repo_url, download_repo
from bot.statesgroup.statesgroup import RepoNameState
from bot.handlers.constants import (START_MES,
                                    GET_USERNAME,
                                    GET_REPO_NAME,
                                    DOWNLOAD_REPO_Q,
                                    DOWNLOAD_ERROR,
                                    DOWNLOAD_SUCCESS,
                                    TRY_DOWNLOAD_AGAIN)


main_router = Router(name=__name__)


@main_router.message(CommandStart())
async def send_start_mes(message: Message) -> None:
    await message.answer(text=START_MES)


@main_router.message(Command('search'))
async def get_username(message: Message, state: FSMContext) -> None:
    await state.set_state(RepoNameState.username)
    await message.answer(text=GET_USERNAME)


@main_router.message(RepoNameState.username)
async def get_repo_name(message: Message, state: FSMContext) -> None:
    await state.update_data(username=message.text)
    await state.set_state(RepoNameState.repo_name)
    await message.answer(text=GET_REPO_NAME)


@main_router.message(RepoNameState.repo_name)
async def check_repo_url(message: Message, state: FSMContext) -> None:
    await state.update_data(repo_name=message.text)
    url_data = await state.get_data()
    await message.answer(text=await render_repo_url(url_data=url_data))
    await message.answer(text=DOWNLOAD_REPO_Q, reply_markup=await get_url_confirm_kb())


@main_router.callback_query(F.data.startswith('right'))
async def handle_right_url(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await callback.message.delete()

    url_data = await state.get_data()
    await state.clear()
    zip_repo_name = await download_repo(url_data=url_data)

    if zip_repo_name:
        repo = FSInputFile(zip_repo_name)
        await callback.message.answer_document(document=repo)
        await del_repo(repo_name=zip_repo_name)
        await callback.message.answer(text=DOWNLOAD_SUCCESS)

    else:
        await callback.message.answer(text=DOWNLOAD_ERROR)


@main_router.callback_query(F.data.startswith('wrong'))
async def handle_wrong_url(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await callback.message.delete()
    await state.clear()
    await callback.message.answer(text=TRY_DOWNLOAD_AGAIN)


@main_router.errors()
async def catch_error(event: ErrorEvent, state: FSMContext) -> None:
    await state.clear()
    logging.warning('Critical error caused by %s', event.exception, exc_info=True)
