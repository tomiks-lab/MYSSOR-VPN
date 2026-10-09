from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from app.config import ADMIN_ID
from app.db import register_user
from app.keyboards import main_menu, plans_menu, admin_menu
router=Router()
PLANS={"month1":("1 месяц",199),"month3":("3 месяца",499),"month12":("12 месяцев",1499)}
@router.message(CommandStart())
async def start(message: Message):
    await register_user(message.from_user.id,message.from_user.username,message.from_user.first_name)
    await message.answer("👋 Добро пожаловать в MYSSOR VPN!\n\nВыберите действие. Оплата и выдача VPN-доступа пока не подключены.",reply_markup=main_menu())
@router.message(Command("admin"))
async def admin(message: Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔ Нет доступа."); return
    await message.answer("🛠 Панель администратора MYSSOR VPN",reply_markup=admin_menu())
@router.message(F.text=="🛒 Купить VPN")
async def buy(message: Message): await message.answer("Выберите тариф:",reply_markup=plans_menu())
@router.callback_query(F.data.startswith("plan:"))
async def plan_selected(callback: CallbackQuery):
    code=callback.data.split(":",1)[1]
    if code not in PLANS:
        await callback.answer("Неизвестный тариф",show_alert=True); return
    title,amount=PLANS[code]
    await callback.message.answer(f"Вы выбрали: {title} — {amount} ₽.\n\nОплата Rolly Pay ещё не подключена. Пока не переводите деньги через этого бота.")
    await callback.answer()
@router.message(F.text=="🔑 Мой VPN")
async def myvpn(message: Message): await message.answer("У вас пока нет выданного VPN-доступа.")
@router.message(F.text=="👤 Профиль")
async def profile(message: Message): await message.answer(f"👤 Ваш профиль\nTelegram ID: {message.from_user.id}")
@router.message(F.text=="📱 Подключение")
async def connect(message: Message): await message.answer("Инструкции появятся после настройки VPN-сервера.")
@router.message(F.text=="🆘 Помощь")
async def help_message(message: Message): await message.answer("🆘 Поддержка MYSSOR VPN. Опишите вопрос администратору.")
@router.message(F.text=="◀️ В главное меню")
async def home(message: Message): await message.answer("Главное меню:",reply_markup=main_menu())
@router.message(F.text.in_({"👥 Пользователи","💰 Продажи","📦 Тарифы","🔑 VPN-ключи","📊 Статистика","📢 Рассылка"}))
async def admin_placeholder(message: Message):
    if message.from_user.id == ADMIN_ID: await message.answer("Этот раздел пока не подключён.")
@router.message()
async def fallback(message: Message): await message.answer("Выберите действие с помощью кнопок меню.",reply_markup=main_menu())
