import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/6d2226149b1f195f3ff84.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝙃𝙚𝙡𝙡𝙤, 𝙄 𝘼𝙢 𝙎𝙪𝙥𝙚𝙧 𝙁𝙖𝙨𝙩 𝙈𝙪𝙨𝙞𝙘 𝙋𝙡𝙖𝙮𝙚𝙧
𝘽𝙤𝙩 𝙁𝙤𝙧 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙂𝙧𝙤𝙪𝙥𝙨 ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ⚡𝐂𝐡𝐚𝐧𝐧𝐞𝐥⚡ : [𝐓𝐇𝐄 𝐏𝐑𝐎𝐅𝐄𝐒𝐒𝐎𝐑 𝐍𝐄𝐓𝐖𝐎𝐑𝐊](https://t.me/THE_PROFESSOR_NETWORK)
┣★ ⚡𝐒𝐮𝐩𝐩𝐨𝐫𝐭⚡ : [⁪⁬⁮╚»𝐓-𝐏-𝗡«╝❥≛⃝🥀❥𝐂𝐇𝐀𝐓 𝐑𝐎𝐎𝐌🖤⃝](https://t.me/MODERN_ELEMENTS)
┣★ ⚡𝐎𝐰𝐧𝐞𝐫⚡   : [𝐀𝐉𝐄𝐄𝐓 𝐆𝐎𝐍𝐃](https://t.me/PAPA_BOL_SAKTEHO)
┗━━━━━━━━━━━━━━━━━┛
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡ ❰ 𝗔𝗱𝗱 𝗠𝗲 𝗜𝗻 𝐘𝐨𝐮𝐫 𝗚𝗿𝗼𝘂𝗽 ❱ ⚡", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "Ajeet", "@papa_bol_sakteho"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/fc4eb9f675176cd2f75fa.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡𝗦𝘂𝗽𝗽𝗼𝗿𝘁⚡", url=f"https://t.me/modern_elements")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["Yuku","Ajeet", "#Channel", "@Channel", "/Channel", "Channel", "@PAPA_BOL_SAKTEHO"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/fc4eb9f675176cd2f75fa.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡𝗖𝗵𝗮𝗻𝗻𝗲𝗹⚡", url=f"https://t.me/The_professor_Network")
                ]
            ]
        ),
    )
