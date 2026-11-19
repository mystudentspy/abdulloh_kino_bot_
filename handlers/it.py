from aiogram import types, filters, Router
rasmlar = [
    "https://i.ytimg.com/vi/9PC1u-B2R3M/maxresdefault.jpg",
]
rt= Router()
@rt.message(filters.Command('it'))
async def it(msg: types.Message):
    await msg.reply("nima gap aka")
    await msg.delete()
    await msg.answer_photo(rasmlar[0])
    print(msg.from_user.id)
    await msg.forward()

