from aiogram import types, filters, Router
rt= Router()
@rt.message()
async def test(msg: types.Message):
    await msg.answer("")

