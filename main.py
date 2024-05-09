import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router

async def main():
    bot = Bot(token="6599832541:AAGXMkBrOo3RR-xGw9WN_01fNSyiBn8p72E")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("Бот выключен")
