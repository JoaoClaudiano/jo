from fastapi import FastAPI
import sqlite3

DB_PATH = "../bot/news.db"
app = FastAPI()

def get_latest_news(limit=5):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, summary, link FROM news ORDER BY published DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [{"title": r[0], "summary": r[1], "link": r[2]} for r in rows]

@app.get("/noticias")
def noticias(limit: int = 5):
    return get_latest_news(limit)