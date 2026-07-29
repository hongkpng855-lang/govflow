"""Debug script to test why gateway Telegram connection hangs"""
import sys, os
sys.path.insert(0, "C:\\Users\\hongk\\.hermes\\hermes-agent")

os.environ["HERMES_HOME"] = "C:\\Users\\hongk\\.hermes"
os.environ["TELEGRAM_BOT_TOKEN"] = open("C:\\Users\\hongk\\.hermes\\.env").read().split("TELEGRAM_BOT_TOKEN=")[1].split("\n")[0].strip()

# Try importing the hermes_plugins telegram adapter
print("1. Importing gateway.run...")
from gateway.run import start_gateway
print("2. Import OK")
import asyncio

print("3. Starting gateway...")
asyncio.run(start_gateway(replace=True))
print("4. Gateway finished")
