from datetime import datetime
from pathlib import Path
from sqlalchemy import BigInteger, DateTime, Integer, String, select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from app.config import DATABASE_URL
if DATABASE_URL.startswith("sqlite"):
    Path("data").mkdir(exist_ok=True)
engine = create_async_engine(DATABASE_URL)
Session = async_sessionmaker(engine, expire_on_commit=False)
class Base(DeclarativeBase): pass
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    username: Mapped[str | None] = mapped_column(String(64), nullable=True)
    first_name: Mapped[str | None] = mapped_column(String(128), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
async def register_user(telegram_id, username, first_name):
    async with Session() as session:
        result = await session.execute(select(User).where(User.telegram_id == telegram_id))
        user = result.scalar_one_or_none()
        if user is None:
            session.add(User(telegram_id=telegram_id, username=username, first_name=first_name))
        else:
            user.username, user.first_name = username, first_name
        await session.commit()
