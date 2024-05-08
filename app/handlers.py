from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import app.currency as currency
import math

import app.keyboards as kb
router = Router()

class Convert(StatesGroup):
    value = State()
    massa = State()

def Converting(value, massa):
    res = massa * 420 / currency.get_usd_rub() + value * 1.04 / currency.get_usd_chy() + 2 + 12
    return f"Итоговая цена: {math.ceil(res)}$ / {math.ceil(res * currency.get_usd_byn())} byn\n\nИтоговая стоимость указана без учета доставки по городам Беларуси. Доставка по РБ рассчитывается исходя из тарифов Европочты."

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text="Привет, это бот компании POIZON RB. Через меня ты можешь оформить заказ или рассичтать цену на товар", reply_markup=kb.start)

@router.callback_query(F.data == "menu")
async def menu(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Привет, это бот компании POIZON RB. Через меня ты можешь оформить заказ или рассичтать цену на товар", reply_markup=kb.start)


@router.callback_query(F.data == "convert")
async def convert(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Выбери категорию товара", reply_markup=kb.category)

@router.callback_query()
async def category(callback: CallbackQuery, state=FSMContext):
    await state.set_state(Convert.value)
    massa = 0
    if callback.data == "shoes_jackets":
        massa = 1.2
    if callback.data == "sweatshirts_pants":
        massa = 0.6
    if callback.data == "bags_backpacks":
        massa = 0.8
    if callback.data == "shirts_shorts":
        massa = 0.3
    if callback.data == "socks_underpants":
        massa = 0.07
    await state.update_data(massa=massa)
    await callback.message.edit_text("Укажите цену в юанях")

@router.message(Convert.value)
async def get_value(message: Message, state=FSMContext):
    try:
        value = float(message.text)
        if value <= 0:
            await state.set_state(Convert.value)
            await message.answer("Введите положительное число\nУкажите цену в юанях")
        else:
            await state.update_data(value=value)
            data = await state.get_data()
            #await message.answer(f"value: {data["value"]}\nmass: {data["res"]}")
            await message.answer(text=Converting(data["value"], data["massa"]), reply_markup=kb.markup)
            await state.clear()
    except ValueError:
        await state.set_state(Convert.value)
        await message.answer("Неверный формат\nУкажите цену в юанях")