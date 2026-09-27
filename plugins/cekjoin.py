# /cekjoin — khusus admin: cek status join seorang pengguna di setiap channel wajib join.
#   /cekjoin            -> cek akun admin sendiri (tanpa pengecualian admin)
#   /cekjoin 123456789  -> cek pengguna dengan ID tersebut
#   balas pesan seseorang dengan /cekjoin -> cek pengirim pesan itu

from pyrogram import filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import Message
from pyrogram import StopPropagation

from bot import Bot
from config import ADMINS, FORCE_SUB_CHANNEL, FORCE_SUB_EXTRA, FORCE_SUB_GROUP


@Bot.on_message(filters.command("cekjoin") & filters.private & filters.user(ADMINS), group=-2)
async def cek_join(client: Bot, message: Message):
    user_id = message.from_user.id
    if len(message.command) > 1 and message.command[1].lstrip("-").isdigit():
        user_id = int(message.command[1])
    elif message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id

    loaded = {i for i, _, _ in getattr(client, "fsub_extra", [])}
    targets = []
    if FORCE_SUB_CHANNEL:
        targets.append(("FORCE_SUB_CHANNEL", FORCE_SUB_CHANNEL, True))
    if FORCE_SUB_GROUP:
        targets.append(("FORCE_SUB_GROUP", FORCE_SUB_GROUP, True))
    for i in FORCE_SUB_EXTRA:
        targets.append(("FORCE_SUB_EXTRA", i, i in loaded))

    lines = [f"<b>Cek wajib join untuk</b> <code>{user_id}</code>", ""]
    if not targets:
        lines.append("Tidak ada channel wajib join yang diatur.")
    for var, chat_id, aktif in targets:
        try:
            title = (await client.get_chat(chat_id)).title
        except Exception as e:
            title = f"(tidak bisa dibuka: {str(e)[:60]})"
        try:
            m = await client.get_chat_member(chat_id, user_id)
            status = f"✅ {m.status}" if m.status in ["creator", "administrator", "member"] else f"❌ {m.status}"
        except UserNotParticipant:
            status = "❌ belum join"
        except Exception as e:
            status = f"⚠️ tidak bisa dicek: {str(e)[:80]}"
        note = "" if aktif else "  (DILEWATI saat bot menyala)"
        lines.append(f"<b>{var}</b> {title}\n<code>{chat_id}</code> → {status}{note}")
    lines += ["", "Admin & owner tidak pernah diminta join.",
              f"Kamu admin: {'ya' if message.from_user.id in ADMINS else 'tidak'}"]
    await message.reply_text("\n".join(lines), quote=True)
    raise StopPropagation
