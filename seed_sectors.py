from database import get_connection

sectors_data = [
    ("NPN.JO", "Naspers", "Technology"),
    ("PRX.JO", "Prosus", "Technology"),
    ("SOL.JO", "Sasol", "Resources/Energy"),
    ("AGL.JO", "Anglo American", "Resources/Mining"),
    ("BHP.JO", "BHP Group", "Resources/Mining"),
    ("FSR.JO", "FirstRand", "Financials"),
    ("SBK.JO", "Standard Bank", "Financials"),
    ("ABG.JO", "Absa Group", "Financials"),
    ("MTN.JO", "MTN Group", "Telecommunications"),
    ("VOD.JO", "Vodacom", "Telecommunications"),
    ("SHP.JO", "Shoprite", "Consumer/Retail"),
    ("WHL.JO", "Woolworths", "Consumer/Retail"),
    ("APN.JO", "Aspen Pharmacare", "Healthcare"),
    ("DSY.JO", "Discovery", "Financials/Insurance"),
    ("CPI.JO", "Capitec", "Financials"),
]

def seed_sectors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT OR REPLACE INTO sectors (ticker, company_name, sector) VALUES (?, ?, ?)",
        sectors_data
    )
    conn.commit()
    conn.close()
    print(f"Seeded {len(sectors_data)} tickers into sectors table.")
    
if __name__ == "__main__":
    seed_sectors()