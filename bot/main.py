from rss_parser import fetch_news
from database import init_db, save_news
from telegram import Bot

TELEGRAM_TOKEN = "SEU_TOKEN_DO_BOT"
CHAT_ID = "SEU_CHAT_ID"

init_db()
bot = Bot(token=TELEGRAM_TOKEN)

for item in fetch_news():
    save_news(item)
    # Envia alerta para Telegram
    bot.send_message(chat_id=CHAT_ID, text=f"Nova notícia: {item['title']}\n{item['link']}")

print("Bot atualizou notícias e enviou alertas!")