# --- Perbaikan untuk Pyrogram 1.4 (versi lama) -----------------------
import time
from threading import Lock

from pyrogram import utils
from pyrogram.session.internals.msg_id import MsgId

# 1) Perbaikan "Peer id invalid" untuk ID channel baru (-1003...)
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

# 2) Perbaikan "[16] The msg_id is too low": pakai jam asli server
_msg_lock = Lock()
_msg_state = {"last": 0}


def _new_msg_id(cls) -> int:
    with _msg_lock:
        msg_id = int(time.time() * 2 ** 32) & ~3
        if msg_id <= _msg_state["last"]:
            msg_id = _msg_state["last"] + 4
        _msg_state["last"] = msg_id
        return msg_id


MsgId.__new__ = staticmethod(_new_msg_id)
# ---------------------------------------------------------------------

from bot import Bot

Bot().run()
