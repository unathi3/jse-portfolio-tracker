from flask import Flask, render_template, request, redirect, url_for
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

DEFAULT_PORTFOLIO_ID = 1

@app.route("/transactions/new", methods=["GET", "POST"])
def new_transaction():
    if request.method == "POST":
        ticker = request.form["ticker"]
        transaction_type = request.form["transaction_type"]
        quantity = request.form["quantity"]
        price_per_share = request.form["price_per_share"]
        transaction_date = request.form["transaction_date"]

        conn = get_connection()
        company_name = conn.execute(
            "SELECT company_name FROM sectors WHERE ticker = ?", (ticker,)
        ).fetchone()["company_name"]

        conn.execute("""
            INSERT INTO transactions
            (portfolio_id, ticker, company_name, transaction_type, quantity, price_per_share, transaction_date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (DEFAULT_PORTFOLIO_ID, ticker, company_name, transaction_type, quantity, price_per_share, transaction_date))
        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    conn = get_connection()
    tickers = conn.execute("SELECT ticker, company_name FROM sectors ORDER BY ticker").fetchall()
    conn.close()
    return render_template("new_transaction.html", tickers=tickers)

if __name__ == "__main__":
    app.run(debug=True)