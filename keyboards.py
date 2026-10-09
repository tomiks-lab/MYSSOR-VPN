from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
def main_menu():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="🛒 Купить VPN")],
        [KeyboardButton(text="🔑 Мой VPN"), KeyboardButton(text="👤 Профиль")],
        [KeyboardButton(text="📱 Подключение"), KeyboardButton(text="🆘 Помощь")],
    ], resize_keyboard=True)
def plans_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⚡ 1 месяц — 199 ₽", callback_data="plan:month1")],
        [InlineKeyboardButton(text="🔥 3 месяца — 499 ₽", callback_data="plan:month3")],
        [InlineKeyboardButton(text="💎 12 месяцев — 1499 ₽", callback_data="plan:month12")],
    ])
def admin_menu():
    rows=[["👥 Пользователи","💰 Продажи"],["📦 Тарифы","🔑 VPN-ключи"],["📊 Статистика","📢 Рассылка"],["◀️ В главное меню"]]
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=x) for x in row] for row in rows], resize_keyboard=True)
