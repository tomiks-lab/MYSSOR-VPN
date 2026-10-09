import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
ADMIN_ID = int(os.getenv("ADMIN_ID", "0") or "0")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./data/myssor.db")
