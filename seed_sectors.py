from database import get_connection

sectors_data = [
    ("NPN.JO", "Technology"),
    ("PRX.JO", "Technology"),
    ("SOL.JO", "Resources/Energy"),
    ("AGL.JO", "Resources/Mining"),
    ("BHP.JO", "Resources/Mining"),
    ("FSR.JO", "Financials"),
    ("SBK.JO", "Financials"),
    ("ABG.JO", "Financials"),
    ("MTN.JO", "Telecommunications"),
    ("VOD.JO", "Telecommunications"),
    ("SHP.JO", "Consumer/Retail"),
    ("WHL.JO", "Consumer/Retail"),
    ("APN.JO", "Healthcare"),
    ("DSY.JO", "Financials/Insurance"),
    ("CPI.JO", "Financials"),
]

def seed_sectors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT OR REPLACE INTO sectors (ticker, sector) VALUES (?, ?)",
        sectors_data
    )
    conn.commit()
    conn.close()
    print(f"Seeded {len(sectors_data)} tickers into sectors table.")

if __name__ == "__main__":
    seed_sectors()