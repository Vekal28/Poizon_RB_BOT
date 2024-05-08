import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router

async def main():
    bot = Bot(token="1851402995:AAE4BFg8EbzQEhy0rJUGeWRY90akM7aMLCM")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("Бот выключен")