#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>☆  𝙾𝚠𝚗𝚎𝚛 : <a href='tg://user?id={OWNER_ID}'>𝙵𝙸𝙻𝙼𝚂 𝙾𝙵 𝙵𝙾𝚁𝚃𝚄𝙽𝙴</a>\n\n☆  𝚄𝚙𝚍𝚊𝚝𝚎𝚜 : @FilmsofFortune\n\n☆  𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝙶𝚛𝚘𝚞𝚙 : @FilmsofFortune</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴 🔒", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
