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
ChooseKoloda = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Колоды гипнотического языка'),
                                             KeyboardButton(text='Колоды "ДА"')]], resize_keyboard=True, input_field_placeholder='Выберите набор колод')

ChooseTheme = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Переговоры'),
                                             KeyboardButton(text='Продажи')],
                                             [KeyboardButton(text='Отношения между мужчиной и женщиной'),
                                             KeyboardButton(text='Отношения между родителями и ребенком')],
                                             [KeyboardButton(text='Продолжить со случайной темой')]], resize_keyboard=True, input_field_placeholder='Выберите тему')