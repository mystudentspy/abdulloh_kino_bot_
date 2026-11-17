from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("rang"))
async def test(msg: types.Message):
  await msg.answer("admin @dizcard rang tanlang (masalan: qizil, ko'k, yashil):")
@rt.message()
async def check_user_text(msg: types.Message):
  # Foydalanuvchi yozgan so'zni kichik harfga o'tkazamiz
  text = msg.text.strip().lower()
  togri_ranglar = ["qizil", "ko'k", "yashil", "sariq"]
  if text in togri_ranglar:
    await msg.answer(f"siz rang tanladiz {msg.text} to'g'ri.")



