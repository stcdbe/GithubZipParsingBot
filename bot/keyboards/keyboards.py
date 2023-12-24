from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_url_confirm_kb() -> InlineKeyboardMarkup:
    btns = [[InlineKeyboardButton(text='Yes', callback_data='right_url'),
             InlineKeyboardButton(text='No', callback_data='wrong_url')]]
    return InlineKeyboardMarkup(inline_keyboard=btns)
