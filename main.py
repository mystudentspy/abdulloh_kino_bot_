import asyncio, logging
from aiogram import Bot, Dispatcher
from config.settings import token
from handlers.start import rt as start
from handlers.help import rt as help
from handlers.rang import rt as rang
from handlers.test import rt as test
from handlers.murojat import rt as murojat
from handlers.mushik import rt as mushik
from handlers.it import rt as it
dp = Dispatcher()

async def main():
    bot = Bot(token)
    # # dp.include_router(test)
    # dp.include_router(start)
    # dp.include_router(help)
    # dp.include_router(rang)
    # dp.include_router(murojat)
    # dp.include_router(mushik)
    dp.include_router(it)




    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
