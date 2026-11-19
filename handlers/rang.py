from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("rang"))
async def test(msg: types.Message):
  await msg.answer("admin @dizcard rang tanlang (masalan: qizil, ko'k, yashil):")




