from aiogram import Bot, F, Router, types

rt = Router()


@rt.message(F.chat.type == "private", F.text)
async def h_private_text(msg: types.Message):
    await msg.answer("Lichkada matn yubordingiz")


@rt.message(F.chat.type == "private", F.photo)
async def h_private_photo(msg: types.Message):
    await msg.answer("Lichkada rasm yubordingiz")


@rt.message(F.chat.type.in_({"group", "supergroup"}), F.sticker)
async def h_group_sticker(msg: types.Message):
    await msg.answer("Guruhda stiker yubordingiz")


@rt.message(F.chat.type.in_({"group", "supergroup"}), F.voice)
async def h_group_voice(msg: types.Message):
    await msg.answer("Guruhda ovozli xabar yubordingiz")


@rt.message(F.chat.type.in_({"group", "supergroup"}), F.animation)
async def h_admin_owner_gif(msg: types.Message, bot: Bot):
    member = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if member.status in {"administrator", "creator"}:
        await msg.answer("Admin/Ega GIF yubordi")


@rt.message(F.chat.type.in_({"group", "supergroup"}), F.video)
async def h_admin_owner_video(msg: types.Message, bot: Bot):
    member = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if member.status in {"administrator", "creator"}:
        await msg.answer("Admin/Ega video yubordi")



@rt.message(F.chat.type.in_({"group", "supergroup"}), F.document)
async def h_owner_doc(msg: types.Message, bot: Bot):
    member = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if member.status == "creator":
        await msg.answer("Guruh egasi hujjat yubordi")



@rt.message(F.chat.type.in_({"group", "supergroup"}), F.audio)
async def h_admin_only_audio(msg: types.Message, bot: Bot):
    member = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if member.status == "administrator":
        await msg.answer("Faqat admin audio yubordi")















