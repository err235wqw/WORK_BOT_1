from aiogram import types
from aiogram.filters import BaseFilter

from create_bot import bot, dp


class IsSubscriber(BaseFilter):
    def __init__(self, a):
        self.a = a

    async def __call__(self, message: types.Message):
        sub = await bot.get_chat_member(chat_id='@testnew29', user_id=message.from_user.id)
        if sub.status != types.ChatMemberLeft:
            return True
        else:
            await dp.bot.send_message(chat_id=message.from_user.id, text=f'Подпишитесь на телеграмм канал:\nhttps://t.me/testnew29')
            return False
