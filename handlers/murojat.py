from aiogram import types, filters, Router
rt= Router()
@rt.message(filters.Command("admin"))
async def test(msg: types.Message):
    await msg.answer("admin murojat uchun @dizcard va @kompusta_ai" )



















































