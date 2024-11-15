from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TipKb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Показать пример", callback_data="tip")],
    [InlineKeyboardButton(
        text="Дальше", callback_data="next")],
    [InlineKeyboardButton(text="Выйти в меню", callback_data='menu')],
])
Next = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Дальше", callback_data="next")],
    [InlineKeyboardButton(text="Выйти в меню", callback_data='menu')]
])