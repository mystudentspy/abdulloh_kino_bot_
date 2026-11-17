from aiogram import types, filters, Router
rt= Router()
@rt.message(filters.Command("help"))
async def test(msg: types.Message):
    await msg.answer("/start , /rang , /admin ,")
