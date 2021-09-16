from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAx0CXXic2wACKj5hJQ-ggzGDbvE85fnQ1yHq3Uz8fgACJwMAAgnXYFRDJl6uBNjr_CAE")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ  ɢʀᴏᴜᴩ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. 
ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜsɪᴄ ғʀᴇᴇʟʏ ᴅᴏɴ'ᴛ ꜰᴏʀɢᴇᴛ ᴛᴏ ᴀᴅᴅ ᴍɪɴᴇ ᴀꜱꜱɪꜱᴛᴀɴᴛ @Venom_Assistant ❤️ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ [ᴢᴀɪᴅ](https://t.me/Timesisnotwaiting) !**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ❣️", url="https://t.me/VENOMxCRAZY")
                  ],[
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ👿", url="https://t.me/Zaid_team1"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url="https://t.me/Zaid_Updates"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "ᴀᴅᴅ ᴍᴇ ɪɴ ᴜʀ ꜱᴇxʏ ɢʀᴘ", url="https://t.me/V3NOM_MUSIC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ᴡʜᴀᴛ ꜰᴏʀ ᴡᴀɪᴛɪɴɢ? ꜱᴛᴀʀᴛ ꜰᴜᴄᴋɪɴɢ ɪɴ ᴠᴄ ʏʀʀ🥴**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊Uᴩᴅᴀᴛᴇs", url="https://t.me/Zaid_Updates")
                ]
            ]
        )
   )
