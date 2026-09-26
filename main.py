# --- Perbaikan "Peer id invalid" untuk ID channel baru (-1003...) ---
# Pyrogram versi lama hanya mengenal ID channel sampai -1002147483647.
from pyrogram import utils

utils.MIN_CHANNEL_ID = -1009999999999


def get_peer_type_new(peer_id: int) -> str:
    peer_id_str = str(peer_id)
    if not peer_id_str.startswith("-"):
        return "user"
    elif peer_id_str.startswith("-100"):
        return "channel"
    else:
        return "chat"


utils.get_peer_type = get_peer_type_new
# ---------------------------------------------------------------------

from bot import Bot

Bot().run()
