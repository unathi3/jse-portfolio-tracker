from flask import Flask, render_template
from database import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    conn = get_connection()
    rows = conn.execute("""
        SELECT s.ticker, s.company_name, s.sector, ph.close_price, ph.date
        FROM sectors s
        LEFT JOIN price_history ph ON s.ticker = ph.ticker
        WHERE ph.id IN (
            SELECT id FROM price_history ph2
            WHERE ph2.ticker = s.ticker
            ORDER BY ph2.fetched_at DESC
            LIMIT 1
        )
        ORDER BY s.ticker
    """).fetchall()
    conn.close()
    return render_template("home.html", stocks=rows)

if __name__ == "__main__":
    app.run(debug=True)

    