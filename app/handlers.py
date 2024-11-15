import os
from aiogram import F, Router, types, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove


import app.keyboards as kb
import app.states as st
import app.sourse as src
import app.feature as ft

router = Router()
SAVE_PATH = 'C:/src/tg_bot_test/app/database'

# region Command


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(src.start_phrase, reply_markup=None)
    await message.answer(src.choose_phrase, reply_markup=None)
    await state.set_state(st.start_state.choose)


# @router.message(Command('help'))
# async def cmd_help(message: Message):
#     await message.answer('Вы попросили помощь, хз, можете помолиться')

# endregion


# region training
@router.message(st.start_state.choose, F.text)
async def start_generate(message: Message, state: FSMContext):
    if message.text == 'Все' or message.text == 'все' or message.text == 'Всё' or message.text == 'всё' or message.text == 'All' or message.text == 'all':
        phrases = await ft.generate_list_of_prases()
    else:
        arr = message.text.split(',')
        fl = True
        for i in arr:
            if i not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                await message.answer('Некорректно введены номера', reply_markup=None)
                return
        phrases = await ft.generate_list_of_prases(map(int, arr))
    await state.set_state(st.start_state.list_of_phrases)
    await state.update_data(list_of_phrases=phrases)
    first = await ft.generate_random_number(len(phrases)-1)
    await state.set_state(st.start_state.cur)
    await state.update_data(cur=first)
    await message.answer(phrases[first][1], reply_markup=kb.TipKb)
    await state.set_state(st.start_state.train)


@router.message(st.start_state.train, F.text)
async def training(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.set_state(st.start_state.prev)
    await state.update_data(prev=data["cur"])
    number = data['cur']
    while number == data['cur']:
        number = await ft.generate_random_number(len(data['list_of_phrases'])-1)
    await state.set_state(st.start_state.cur)
    await state.update_data(cur=number)
    await message.answer(data['list_of_phrases'][number][1], reply_markup=kb.TipKb)
    await state.set_state(st.start_state.train)


@router.callback_query()
async def heandler_callback(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if call.data == 'tip':
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
        await call.message.answer(data['list_of_phrases'][number][1], reply_markup=kb.TipKb)
        await call.answer()
        await state.set_state(st.start_state.train)
    elif call.data == 'menu':
        await call.message.answer(src.start_phrase, reply_markup=None)
        await call.message.answer(src.choose_phrase, reply_markup=None)
        await state.set_state(st.start_state.choose)


# endregion
# region gen_product_description


# @router.message(F.text == 'Создание описания и карточки AI')
# async def start_text(message: Message, state: FSMContext):
#     await state.set_state(gen_desk.product_name)
#     await message.answer('Введите название товара', reply_markup=types.ReplyKeyboardRemove())


# @router.message(F.text == 'Веб-интерфейс')
# async def start_text(message: Message):


# @router.message(gen_desk.product_name)
# async def product_name(message: Message, state: FSMContext):
#     await state.update_data(product_name=message.text)
#     await state.set_state(gen_desk.gender)
#     await message.answer('Для: мужчин, женщин, унисекс?')


# @router.message(gen_desk.gender)
# async def product_name(message: Message, state: FSMContext):
#     await state.update_data(gender=message.text)
#     await state.set_state(gen_desk.size)
#     await message.answer('Укажите размер товара')


# @router.message(gen_desk.size)
# async def product_name(message: Message, state: FSMContext):
#     await state.update_data(size=message.text)
#     await state.set_state(gen_desk.phrase)
#     await message.answer('Введите клюючевую фразу товара')


# @router.message(gen_desk.phrase)
# async def product_name(message: Message, state: FSMContext):
#     await state.update_data(phrase=message.text)
#     await state.set_state(Generate.text)
#     data = await state.get_data()
#     response = await text_gpt(f'Сгенерируй описание для товара интернет магазина по такому описанию: Название товара - {data["product_name"]}, он для {data["gender"]}, размеры в наличии - {data["size"]}, а еще этот товар {data["phrase"]}')
#     await message.answer(response.choices[0].message.content, reply_markup=kb.choose)
#     await state.set_state(gen_desk.img)


# @router.message(gen_desk.img, F.text == 'Сгенерировать')
# async def genimg(message: Message, state: FSMContext):
#     await state.set_state(Generate.image)
#     data = await state.get_data()
#     description = f'Сгенерируй карточку для товара интернет магазина в реалистичном стиле по такому описанию: Название товара - {
#         data["product_name"]}, он для {data["gender"]}, размеры в наличии - {data["size"]}, а еще этот товар {data["phrase"]}'
#     image_path = await image_gpt(description)
#     await message.answer_photo(image_path, reply_markup=kb.choose)
#     await state.set_state(gen_desk.img)


# @router.message(gen_desk.img, F.text == 'В меню')
# async def menu(message: Message, state: FSMContext):
#     await message.answer('Вернуться в меню', reply_markup=kb.main)
#     await state.clear()


# @router.message(Generate.text)
# async def text_error(message: Message):
#     await message.answer('Подождите, описание товара еще генерируется...')


# @router.message(Generate.image)
# async def text_error(message: Message):
#     await message.answer('Подождите, карточка товара еще генерируется...')

# endregion

# region gen_product_image


# @router.message(F.text == 'Генерация изображения по исходнику')
# async def start_text(message: Message):
#     await message.answer('Функция в разработке', reply_markup=kb.main)


# @router.message(gen_img.product_name)
# async def product_name(message: Message, state: FSMContext):
#     await state.update_data(product_name=message.text)
#     await state.set_state(gen_img.gender)
#     await message.answer('Для: мужчин, женщин, унисекс?')


# @router.message(gen_img.gender)
# async def product_name(message: Message, state: FSMContext):
#     await state.update_data(gender=message.text)
#     await state.set_state(gen_img.size)
#     await message.answer('Укажите размер товара')


# @router.message(gen_img.size)
# async def product_name(message: Message, state: FSMContext):
#     await state.update_data(size=message.text)
#     await state.set_state(gen_img.color)
#     await message.answer('Введите основной цвет')


# @router.message(gen_img.color)
# async def product_name(message: Message, state: FSMContext):
#     await state.update_data(color=message.text)
#     await state.set_state(gen_img.phrase)
#     await message.answer('Введите описание изменений на карточке')


# @router.message(gen_img.phrase)
# async def product_name(message: Message, state: FSMContext):
#     await state.update_data(phrase=message.text)
#     await state.set_state(gen_img.image)
#     await message.answer('Пришлите фотографию вашего товара')


# @router.message(gen_img.image, F.photo)
# async def edit_photo(message: Message, state: FSMContext, bot: Bot):
#     print("Скачивание фото")
#     photo = message.photo[-1]
#     file_info = await bot.get_file(photo.file_id)
#     file_path = file_info.file_path
#     file_name = f"{message.from_user.id}_{file_info.file_unique_id}.jpg"
#     save_location = os.path.join(SAVE_PATH, file_name)
#     # Скачивание и сохранение файла
#     await bot.download_file(file_path, save_location)

#     data = await state.get_data()
#     description = f'Добавь на картинку и аккуратно расположи так, чтобы не перекрывать основной обьект на картинке: название товара - {data["product_name"]}, что он для {
#         data["gender"]},добваь небольшую надпись про размеры в наличии - {data["size"]}, а еще добавь, что он {data["phrase"]}, все сделай надписями в одном красивом подходящем стиле и используй цвет надписей {data["color"]}'
#     image_path = await image_gpt("C:/src/tg_bot_test/app/database/1.png", description)
#     print(image_path)
#     await message.answer_photo(image_path)


# @router.message(Generate.image)
# async def text_error(message: Message):
#     await message.answer(photo='Подождите, карточка товара еще генерируется...')

# endregion
