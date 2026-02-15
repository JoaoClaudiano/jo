from rss_parser import fetch_news
from database import init_db, save_news
from telegram import Bot
import asyncio
import websockets
import json

TELEGRAM_TOKEN = "7609273579:AAFfs9gU0EMC6vAaWU7Hyqj0KMtmzJWIcmw"
CHAT_ID = "SEU_CHAT_ID"
WS_SERVER = "ws://localhost:8001"  # WebSocket API

init_db()
bot = Bot(token=7609273579:AAFfs9gU0EMC6vAaWU7Hyqj0KMtmzJWIcmw)

async def notify_ws(message):
    async with websockets.connect(WS_SERVER) as ws:
        await ws.send(json.dumps(message))

async def main_loop():
    while True:
        for item in fetch_news():
            if save_news(item):
                # envia alerta para Telegram
                bot.send_message(chat_id=CHAT_ID, text=f"Nova notícia: {item['title']}\n{item['link']}")
                # envia alerta para WebSocket
                await notify_ws({"title": item["title"], "summary": item["summary"], "link": item["link"]})
        await asyncio.sleep(300)  # verifica a cada 5 minutos

asyncio.run(main_loop())