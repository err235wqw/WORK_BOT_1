from aiogram import F, Dispatcher, types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender

from create_bot import dp, bot
from keyboards import client_kb as kb
from states import client_st as st
from filters import IsSubscriber

import app.sourse as src
import app.feature as ft


async def command_start(message: Message, state: FSMContext):
    sub = await bot.get_chat_member(chat_id='@testnew29', user_id=message.from_user.id)
    if sub.status == 'left':
        await message.answer(f'Подпишитесь на телеграмм канал:\nhttps://t.me/testnew29', reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(src.start_phrase, reply_markup=kb.ChooseKoloda)
        await state.set_state(st.start_state.start)


async def command_help(message: Message):
    sub = await bot.get_chat_member(chat_id='@testnew29', user_id=message.from_user.id)
    if sub.status == 'left':
        await message.answer(f'Подпишитесь на телеграмм канал:\nhttps://t.me/testnew29', reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer('Вы попросили помощь, хз, можете помолиться')


# region Start
async def start_generate_standart(message: Message, state: FSMContext):
    sub = await bot.get_chat_member(chat_id='@testnew29', user_id=message.from_user.id)
    if sub.status == 'left':
        await message.answer(f'Подпишитесь на телеграмм канал:\nhttps://t.me/testnew29', reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(src.choose_phrase_start, reply_markup=ReplyKeyboardRemove())
        await state.set_state(st.start_state.Da)
        await state.update_data(Da=False)
        await state.set_state(st.start_state.choose)


async def start_generate_da(message: Message, state: FSMContext):
    sub = await bot.get_chat_member(chat_id='@testnew29', user_id=message.from_user.id)
    if sub.status == 'left':
        await message.answer(f'Подпишитесь на телеграмм канал:\nhttps://t.me/testnew29', reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(src.choose_phrase_da, reply_markup=ReplyKeyboardRemove())
        await state.set_state(st.start_state.Da)
        await state.update_data(Da=True)
        await state.set_state(st.start_state.choose)
# endregion


# region training
async def start_generate(message: Message, state: FSMContext):
    sub = await bot.get_chat_member(chat_id='@testnew29', user_id=message.from_user.id)
    if sub.status == 'left':
        await message.answer(f'Подпишитесь на телеграмм канал:\nhttps://t.me/testnew29', reply_markup=ReplyKeyboardRemove())
    else:
        data = await state.get_data()
        Da = data.get('Da', False)
        if message.text == 'Все' or message.text == 'все' or message.text == 'Всё' or message.text == 'всё' or message.text == 'All' or message.text == 'all':
            phrases = await ft.generate_list_of_prases(Da=Da)
        else:
            arr = message.text.split(',')
            fl = True
            for i in arr:
                if i not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                    await message.answer('Некорректно введены номера', reply_markup=None)
                    return
            phrases = await ft.generate_list_of_prases(map(int, arr), Da=Da)
        theme_number = await ft.generate_random_number(99)
        await state.set_state(st.start_state.theme_number)
        await state.update_data(theme_number=theme_number)
        await state.set_state(st.start_state.list_of_phrases)
        await state.update_data(list_of_phrases=phrases)
        first = await ft.generate_random_number(len(phrases)-1)
        await state.set_state(st.start_state.cur)
        await state.update_data(cur=first)
        await message.answer(src.problems[theme_number], reply_markup=None)
        await message.answer(phrases[first][1], reply_markup=kb.TipKb)
        await state.set_state(st.start_state.train)


async def training(message: Message, state: FSMContext):
    sub = await bot.get_chat_member(chat_id='@testnew29', user_id=message.from_user.id)
    if sub.status == 'left':
        await message.answer(f'Подпишитесь на телеграмм канал:\nhttps://t.me/testnew29', reply_markup=ReplyKeyboardRemove())
    else:
        data = await state.get_data()
        await state.set_state(st.start_state.prev)
        await state.update_data(prev=data["cur"])
        number = data['cur']
        while number == data['cur']:
            number = await ft.generate_random_number(len(data['list_of_phrases'])-1)
        await state.set_state(st.start_state.cur)
        await state.update_data(cur=number)
        await message.answer(src.problems[data.get('theme_number', 0)], reply_markup=None)
        await message.answer(data['list_of_phrases'][number][1], reply_markup=kb.TipKb)
        await state.set_state(st.start_state.train)


async def heandler_callback(call: CallbackQuery, state: FSMContext):
    sub = await bot.get_chat_member(chat_id='@testnew29', user_id=call.message.from_user.id)
    if sub.status == 'left':
        await call.message.answer(f'Подпишитесь на телеграмм канал:\nhttps://t.me/testnew29', reply_markup=ReplyKeyboardRemove())
    else:
        data = await state.get_data()
        if call.data == 'tip':
            await call.message.answer(src.problems[data.get('theme_number', 0)], reply_markup=None)
            await call.message.answer(data['list_of_phrases'][data['cur']][2], reply_markup=kb.Next)
            await call.answer()
        elif call.data == 'next':
            await state.set_state(st.start_state.prev)
            await state.update_data(prev=data["cur"])
            number = data['cur']
            while number == data['cur']:
                number = await ft.generate_random_number(len(data['list_of_phrases'])-1)
            await state.set_state(st.start_state.cur)
            await state.update_data(cur=number)
            await call.message.answer(src.problems[data.get('theme_number', 0)], reply_markup=None)
            await call.message.answer(data['list_of_phrases'][number][1], reply_markup=kb.TipKb)
            await call.answer()
            await state.set_state(st.start_state.train)
        elif call.data == 'menu':
            await call.message.answer(src.start_phrase, reply_markup=kb.ChooseKoloda)
            await state.set_state(st.start_state.start)
        elif call.data == 'change_theme':
            theme_number = data.get('theme_number', 0)
            while theme_number == data.get('theme_number', 0):
                theme_number = await ft.generate_random_number(99)
            await state.set_state(st.start_state.theme_number)
            await state.update_data(theme_number=theme_number)

            await state.set_state(st.start_state.prev)
            await state.update_data(prev=data["cur"])
            number = data['cur']
            while number == data['cur']:
                number = await ft.generate_random_number(len(data['list_of_phrases'])-1)
            await state.set_state(st.start_state.cur)
            await state.update_data(cur=number)
            await call.message.answer(src.new_theme, reply_markup=None)
            await call.message.answer(src.problems[theme_number], reply_markup=None)
            await call.message.answer(data['list_of_phrases'][number][1], reply_markup=kb.TipKb)
            await call.answer()
            await state.set_state(st.start_state.train)
# endregion


def register_handlers_client(dp: Dispatcher):
    dp.message.register(command_start, Command('start'),
                        )
    dp.message.register(command_help, Command('help'),
                        )
    dp.message.register(start_generate_standart, st.start_state.start,
                        F.text == 'Стандартные колоды')
    dp.message.register(start_generate_da, st.start_state.start,
                        F.text == 'Колоды "ДА"')
    dp.message.register(
        start_generate, st.start_state.choose, F.text)
    dp.message.register(training, st.start_state.train,
                        F.text)
    dp.callback_query.register(
        heandler_callback)
