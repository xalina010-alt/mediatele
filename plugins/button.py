# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def _join_buttons(client, prefix):
    """Tombol semua channel/grup wajib join: 2 per baris."""
    btns = []
    if FORCE_SUB_CHANNEL:
        btns.append(InlineKeyboardButton(text=f"{prefix}Channel", url=client.invitelink))
    if FORCE_SUB_GROUP:
        btns.append(InlineKeyboardButton(text=f"{prefix}Grup", url=client.invitelink2))
    for _chat_id, title, link in getattr(client, "fsub_extra", []):
        btns.append(InlineKeyboardButton(text=f"{prefix}{title}"[:40], url=link))
    return [btns[i : i + 2] for i in range(0, len(btns), 2)]


def start_button(client):
    buttons = [[InlineKeyboardButton(text="Informasi Bot", callback_data="about")]]
    buttons += _join_buttons(client, "")
    buttons.append([InlineKeyboardButton(text="Tutup", callback_data="close")])
    return buttons


def fsub_button(client, message):
    buttons = _join_buttons(client, "Join ")
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text="Coba Lagi",
                    url=f"https://t.me/{client.username}?start={message.command[1]}",
                )
            ]
        )
    except IndexError:
        pass
    return buttons
