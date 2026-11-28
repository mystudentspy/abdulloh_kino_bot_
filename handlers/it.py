import re
from aiogram import F, Router, filters, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

rt = Router()


class CarState(StatesGroup):
    car_name = State()
    car_color = State()
    car_year = State()
    car_price = State()
    car_photo = State()


def is_only_letters(text: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-zА-Яа-яЁёЎўҚқҒғҲҳʼ’ʻ\s-]+", text.strip()))


@rt.message(filters.Command("add_car"), F.chat.type == "private")
async def start_car(msg: types.Message, state: FSMContext):
    await state.clear()
    await state.set_state(CarState.car_name)
    await msg.answer("Mashina rusumini kiriting (faqat harf, masalan: Gentra):")


@rt.message(filters.StateFilter(CarState.car_name), F.chat.type == "private", F.text, ~F.text.startswith("/"))
async def get_name(msg: types.Message, state: FSMContext):
    name = msg.text.strip()
    if len(name) < 2 or not is_only_letters(name):
        await msg.answer("Mashina nomi faqat harflardan iborat bo'lishi kerak. Qayta yozing:")
        return

    await state.update_data(car_name=name)
    await state.set_state(CarState.car_color)
    await msg.answer("Rangini kiriting (faqat harf, masalan: Oq):")


@rt.message(filters.StateFilter(CarState.car_color), F.chat.type == "private", F.text, ~F.text.startswith("/"))
async def get_color(msg: types.Message, state: FSMContext):
    color = msg.text.strip()
    if len(color) < 2 or not is_only_letters(color):
        await msg.answer("Rang faqat harflardan iborat bo'lishi kerak. Qayta yozing:")
        return

    await state.update_data(car_color=color)
    await state.set_state(CarState.car_year)
    await msg.answer("Chiqqan yilini kiriting (faqat raqam, masalan: 2023):")


@rt.message(filters.StateFilter(CarState.car_year), F.chat.type == "private", F.text, ~F.text.startswith("/"))
async def get_year(msg: types.Message, state: FSMContext):
    year_text = msg.text.strip()
    if not year_text.isdigit() or not (1900 <= int(year_text) <= 2026):
        await msg.answer("Yil faqat raqamda (1900–2026) bo'lishi kerak. Qayta yozing:")
        return

    await state.update_data(car_year=int(year_text))
    await state.set_state(CarState.car_price)
    await msg.answer("Narxini kiriting ($ da, faqat raqam, masalan: 12000):")


@rt.message(filters.StateFilter(CarState.car_price), F.chat.type == "private", F.text, ~F.text.startswith("/"))
async def get_price(msg: types.Message, state: FSMContext):
    price_text = msg.text.strip()
    if not price_text.isdigit() or int(price_text) <= 0:
        await msg.answer("Narx faqat musbat raqam bo'lishi kerak. Qayta yozing:")
        return

    await state.update_data(car_price=int(price_text))
    await state.set_state(CarState.car_photo)
    await msg.answer("Mashina rasmini yuboring:")


@rt.message(filters.StateFilter(CarState.car_photo), F.chat.type == "private", F.photo)
async def get_photo(msg: types.Message, state: FSMContext):
    photo_id = msg.photo[-1].file_id
    data = await state.get_data()

    caption = (
        f"<b>Yangi e'lon:</b>\n\n"
        f"<b>Nomi:</b> {data['car_name']}\n"
        f"<b>Rangi:</b> {data['car_color']}\n"
        f"<b>Yili:</b> {data['car_year']}\n"
        f"<b>Narxi:</b> {data['car_price']}$"
    )

    await msg.answer_photo(photo=photo_id, caption=caption, parse_mode="HTML")
    await state.clear()