import sqlite3

DB_PATH = "news.db"

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            summary TEXT,
            link TEXT NOT NULL,
            published DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_news(item):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM news WHERE link = ?", (item['link'],))
    if cursor.fetchone() is None:
        cursor.execute(
            "INSERT INTO news (title, summary, link) VALUES (?, ?, ?)",
            (item['title'], item['summary'], item['link'])
        )
        conn.commit()
        conn.close()
        return True  # nova notícia
    conn.close()
    return False