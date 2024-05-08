from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btn1 = InlineKeyboardButton(text="Калькулятор", callback_data="convert")
btn2 = InlineKeyboardButton(text="Поддержка", url="https://t.me/trivia_manager")
btn3 = InlineKeyboardButton(text="Канал в телеграме", url="https://t.me/poizonrb")
btn4 = InlineKeyboardButton(text="Оформить заказ", url="https://t.me/trivia_manager")
btn5 = InlineKeyboardButton(text="Главное меню", callback_data="menu")
btn6 = InlineKeyboardButton(text="Отзывы", url="https://t.me/poizon_rb_feedback")
btn_1 = InlineKeyboardButton(text="Обувь/куртки", callback_data="shoes_jackets")
btn_2 = InlineKeyboardButton(text="Кофты/штаны", callback_data="sweatshirts_pants")
btn_3 = InlineKeyboardButton(text="Сумки/рюкзаки", callback_data="bags_backpacks")
btn_4 = InlineKeyboardButton(text="Футболки/шорты", callback_data="shirts_shorts")
btn_5 = InlineKeyboardButton(text="Носки/трусы", callback_data="socks_underpants")
btn_6 = InlineKeyboardButton(text="Другое", url="https://t.me/trivia_manager")

start = InlineKeyboardMarkup(inline_keyboard=[[btn1], [btn2], [btn3], [btn6]])

category = InlineKeyboardMarkup(inline_keyboard=[[btn_1, btn_2],[btn_3, btn_4],[btn_5, btn_6]])

markup = InlineKeyboardMarkup(inline_keyboard=[[btn5, btn4]])