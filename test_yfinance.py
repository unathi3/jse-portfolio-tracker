import yfinance as yf

tickers = ["NPN.JO", "SOL.JO", "FSR.JO", "SBK.JO"] #these are the tickers for the companies i want the share prices of

for ticker in tickers: #for each ticker in my array of tickers
    stock = yf.Ticker(ticker)
    info = stock.info
    price_cents = info.get("currentPrice") or info.get("regularMarketPrice") 
    price_rand = price_cents / 100 #JSe prices from yfinance are in cents, convert to Rands
    name = info.get("longName", "Unknown")
    print(f"{ticker} ({name}): R{price_rand:.2f}")


# Historical data for naspers closing prices, also converted to rands
history = yf.Ticker("NPN.JO").history(period="1mo")
history["Close_ZAR"] = history["Close"] / 100
print(history[["Close"]].tail())