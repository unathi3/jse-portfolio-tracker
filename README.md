# JSE Portfolio Tracker

A Flask and SQLite web app for tracking a share portfolio on the Johannesburg Stock Exchange (JSE).
It records buy and sell transactions, pulls current prices with yfinance, and shows holdings,
gain or loss, and sector diversification.

## Run it on your computer

1. Open a terminal in this folder.
2. Create a virtual environment: `python -m venv .venv`
3. Activate it. Windows: `.venv\Scripts\activate`. Mac or Linux: `source .venv/bin/activate`
4. Install the packages: `pip install -r requirements.txt`
5. Start the app: `python app.py`
6. Open http://127.0.0.1:5000 in your browser.

## Use it

1. Create a portfolio on the home page.
2. Add a buy transaction. Type the ticker without ".JO" (for example NPN). Price is Rand per share.
3. Go to Sectors and give each ticker a sector (for example Financials).
4. Open the portfolio and press "Refresh prices". This calls yfinance and saves each price.
5. The holdings table, totals and sector bars now show current values.

## Run the tests

`pytest -v`

The tests never call the internet. They replace the price lookup with fake prices.

## Run it in Docker

1. Install Docker Desktop.
2. Build the image: `docker build -t jse-portfolio-tracker .`
3. Run it: `docker run -p 5000:5000 -v jse-data:/data -e FLASK_SECRET_KEY=change-me jse-portfolio-tracker`
4. Open http://127.0.0.1:5000

The `-v jse-data:/data` part keeps your database when the container stops.

## Files

- `app.py`: the Flask app and every route
- `calc.py`: holdings, average cost, gain or loss, sector breakdown (no Flask code, so it is easy to test)
- `prices.py`: ticker clean-up, cents-to-Rand fix, yfinance lookup
- `db.py` and `schema.sql`: database connection and the four tables
- `templates/` and `static/`: pages and styling
- `tests/`: pytest tests
- `Dockerfile` and `.dockerignore`: container setup
- `.github/workflows/ci.yml`: runs the tests and a Docker build on every push
- `wsgi.py`: entry point used by gunicorn inside Docker

## How the numbers work

Average-cost method. Each buy adds to the share count and total cost (price x quantity + fees).
Each sell removes shares at the current average cost, and the difference between the sale
proceeds and that cost is the realised gain. Unrealised gain is market value minus remaining cost.
Selling more shares than you hold on a given date is rejected.
