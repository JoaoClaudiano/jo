from fastapi import FastAPI, WebSocket
import sqlite3

app = FastAPI()
DB_PATH = "../bot/news.db"
connections = []

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

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    connections.append(ws)
    try:
        while True:
            await ws.receive_text()  # manter conexão
    except:
        connections.remove(ws)