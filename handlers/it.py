from aiogram import types, filters, Router
rt= Router()
@rt.message()
async def test(msg: types.Message):
    print(msg.forward_date)
    print(msg.forward_from)
    print(msg.forward_from_chat)
    await msg.answer(str(msg.text)) , msg.answer(str(msg.date )) , msg.answer(str(msg.date.hour + 5)) , msg.answer(str(msg.date.year))
    await msg.answer(f"{msg.date.hour}:{msg.date.minute}:{msg.date.second:02}")
    # print(msg.chat)
    id = msg.chat.id
    ism = msg.chat.first_name
    await msg.answer(f"id: {id}, ism: {ism}")
    print(msg.from_user)
    if msg.reply_to_message:
        await msg.answer("siz reply qildingiz")
    elif msg.pinned_message:
        await msg.answer("siz xabarni pinga qo'ydingiz")
    else:
        await msg.answer("hech nima")

