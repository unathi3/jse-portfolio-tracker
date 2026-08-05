import yfinance as yf
from datetime import datetime, timezone
from database import get_connection

def get_supported_tickers():
    conn = get_connection()
    rows = conn.execute("SELECT ticker FROM sectors").fetchall()
    conn.close()
    return [row["ticker"] for row in rows]

def fetch_and_store_prices():
    tickers = get_supported_tickers()
    conn = get_connection()
    cursor = conn.cursor()
    fetched_at = datetime.now(timezone.utc).isoformat()

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        price_cents = info.get("currentPrice") or info.get("regularMarketPrice")

        if price_cents is None:
            print(f"Skipping {ticker} — no price data returned")
            continue

        price_rand = price_cents / 100  # JSE prices from yfinance are in cents
        today = datetime.now().strftime("%Y-%m-%d")

        cursor.execute(
            """INSERT INTO price_history (ticker, date, close_price, fetched_at)
               VALUES (?, ?, ?, ?)""",
            (ticker, today, price_rand, fetched_at)
        )
        print(f"{ticker}: R{price_rand:.2f}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    fetch_and_store_prices()