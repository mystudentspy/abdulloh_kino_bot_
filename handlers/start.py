from aiogram import types, filters, Router
rt= Router()
@rt.message(filters.Command("start"))
async def test(msg: types.Message):
    await msg.answer("hush kelib siz /help")

