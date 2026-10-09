from aiogram import Bot, Dispatcher
from app.config import BOT_TOKEN
from app.db import init_db
from app.handlers import router
async def main():
    if not BOT_TOKEN: raise RuntimeError("BOT_TOKEN пуст. Создайте .env и укажите токен.")
    await init_db()
    bot=Bot(token=BOT_TOKEN)
    dp=Dispatcher()
    dp.include_router(router)
    try: await dp.start_polling(bot)
    finally: await bot.session.close()
