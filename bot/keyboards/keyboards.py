from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def checkkb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb1 = InlineKeyboardButton(text='Yes', callback_data='right')
    kb2 = InlineKeyboardButton(text='No', callback_data='wrong')
    kb.add(kb1, kb2)
    return kb
