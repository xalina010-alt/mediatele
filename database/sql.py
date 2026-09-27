import threading
from datetime import datetime, timedelta

from sqlalchemy import TEXT, Column, DateTime, Numeric, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from config import DB_URI


def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8", pool_pre_ping=True)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()

INSERTION_LOCK = threading.RLock()


class Broadcast(BASE):
    __tablename__ = "broadcast"
    id = Column(Numeric, primary_key=True)
    user_name = Column(TEXT)

    def __init__(self, id, user_name):
        self.id = id
        self.user_name = user_name


Broadcast.__table__.create(checkfirst=True)


#  Add user details -
async def add_user(id, user_name):
    with INSERTION_LOCK:
        msg = SESSION.query(Broadcast).get(id)
        if not msg:
            usr = Broadcast(id, user_name)
            SESSION.add(usr)
            SESSION.commit()


async def full_userbase():
    users = SESSION.query(Broadcast).all()
    SESSION.close()
    return users


async def query_msg():
    try:
        return SESSION.query(Broadcast.id).order_by(Broadcast.id)
    finally:
        SESSION.close()


# ---------------------------------------------------------------- pengguna aktif
class UserActivity(BASE):
    """Kapan tiap pengguna pertama dan terakhir kali memakai bot (waktu UTC)."""

    __tablename__ = "user_activity"
    id = Column(Numeric, primary_key=True)
    first_seen = Column(DateTime, nullable=False)
    last_seen = Column(DateTime, nullable=False, index=True)


UserActivity.__table__.create(checkfirst=True)

# Supaya database tidak ditulis di setiap pesan: satu pengguna dicatat paling sering tiap 5 menit.
_TOUCH_EVERY = timedelta(minutes=5)
_last_touch = {}


async def touch_user(id):
    now = datetime.utcnow()
    prev = _last_touch.get(id)
    if prev and now - prev < _TOUCH_EVERY:
        return
    if len(_last_touch) > 50000:
        _last_touch.clear()
    _last_touch[id] = now
    with INSERTION_LOCK:
        try:
            row = SESSION.query(UserActivity).get(id)
            if row:
                row.last_seen = now
            else:
                SESSION.add(UserActivity(id=id, first_seen=now, last_seen=now))
            SESSION.commit()
        except Exception:
            SESSION.rollback()
            raise
        finally:
            SESSION.close()


async def count_users():
    try:
        return SESSION.query(func.count(Broadcast.id)).scalar() or 0
    finally:
        SESSION.close()


async def count_active(hours):
    since = datetime.utcnow() - timedelta(hours=hours)
    try:
        return (
            SESSION.query(func.count(UserActivity.id))
            .filter(UserActivity.last_seen >= since)
            .scalar()
            or 0
        )
    finally:
        SESSION.close()


async def count_new(hours):
    since = datetime.utcnow() - timedelta(hours=hours)
    try:
        return (
            SESSION.query(func.count(UserActivity.id))
            .filter(UserActivity.first_seen >= since)
            .scalar()
            or 0
        )
    finally:
        SESSION.close()
