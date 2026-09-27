# Mencatat pengguna yang aktif memakai bot. Statistiknya hanya bisa dilihat admin lewat /users.
# group=-1: jalan duluan dan tidak menghalangi handler lain.

from pyrogram import filters
from pyrogram.types import CallbackQuery, Message

from bot import Bot
from database.sql import touch_user


async def _touch(client, user):
    if not user or user.is_bot:
        return
    try:
        await touch_user(user.id)
    except Exception as e:
        client.LOGGER(__name__).warning(f"gagal mencatat pengguna aktif: {e}")


@Bot.on_message(filters.private & filters.incoming, group=-1)
async def track_message(client: Bot, message: Message):
    await _touch(client, message.from_user)


@Bot.on_callback_query(group=-1)
async def track_callback(client: Bot, query: CallbackQuery):
    await _touch(client, query.from_user)
