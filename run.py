from handlers import client, admin, other
from create_bot import dp, bot
from asyncio import run


async def on_startup():
    print('Бот запустился')


async def main():
    client.register_handlers_client(dp)
    # admin.register_handlers_client(dp)
    # other.register_handlers_client(dp)
    await dp.start_polling(bot, on_startup=on_startup)

if __name__ == '__main__':
    try:
        run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
