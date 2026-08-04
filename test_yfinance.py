import yfinance as yf

tickers = ["NPN.JO", "SOL.JO", "FSR.JO", "SBK.JO"]

for ticker in tickers:
    stock = yf.Ticker(ticker)
    info = stock.info
    price = info.get("currentPrice") or info.get("regularMarketPrice")
    name = info.get("longName", "Unknown")
    print(f"{ticker} ({name}): R{price}")



history = yf.Ticker("NPN.JO").history(period="1mo")
print(history[["Close"]].tail())