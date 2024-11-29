from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

TipKb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Показать пример", callback_data="tip")],
    [InlineKeyboardButton(
        text="Дальше", callback_data="next")],
    [InlineKeyboardButton(text="Выйти в меню", callback_data='menu')],
    [InlineKeyboardButton(text='Сменить тему', callback_data='change_theme')],
])
Next = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Дальше", callback_data="next")],
    [InlineKeyboardButton(text="Выйти в меню", callback_data='menu')],
    [InlineKeyboardButton(text='Сменить тему', callback_data='change_theme')],
])
ChooseKoloda = ReplyKeyboardMarkup([[KeyboardButton(text='Стандартные колоды'),
                                    KeyboardButton(text='Колоды "ДА"')],
])

