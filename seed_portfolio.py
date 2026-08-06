from datetime import datetime
from database import get_connection

def seed_portfolio():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO portfolios (name, created_at) VALUES (?, ?)",
        ("My JSE Portfolio", datetime.now().isoformat())
    )
    conn.commit()
    print(f"Created portfolio with id {cursor.lastrowid}")
    conn.close()

if __name__ == "__main__":
    seed_portfolio()