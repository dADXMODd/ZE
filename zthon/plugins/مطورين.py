import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["المطورين","مودي"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/0efbb39bb4267911d50f3.jpg",
        caption=f"""• | مطورين سورس زد إي""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مودي ", url=f"https://t.me/UP_UO"),
                    InlineKeyboardButton(
                        "داد مودي ♡", url=f"https://t.me/UP_UO"),
                ],
                [
                   InlineKeyboardButton(
                        "refz ", url=f"https://t.me/UI_9U"),
                ],       
            ]
        ),
    )
    