import asyncio, os
# Read token from .env
with open("C:\\Users\\hongk\\.hermes\\.env") as f:
    for line in f:
        line = line.strip()
        if line.startswith("TELEGRAM_BOT_TOKEN="):
            token = line.split("=", 1)[1]
            break

from telegram import Bot
from telegram.request import HTTPXRequest

async def test():
    print("Testing Telegram connection...")
    request = HTTPXRequest(connection_pool_size=1, connect_timeout=10, read_timeout=10)
    bot = Bot(token=token, request=request)
    try:
        me = await bot.get_me()
        print(f"OK! Bot: @{me.username}")
    except Exception as e:
        print(f"FAILED: {type(e).__name__}: {e}")

asyncio.run(test())
