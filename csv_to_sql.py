import sqlite3
import pandas as pd

# Read CSV
df = pd.read_csv("weather_data.csv")

# Connect to SQLite DB (creates file if it doesn't exist)
conn = sqlite3.connect("weather.db")

# Write DataFrame to SQL table
df.to_sql("weather", conn, if_exists="replace", index=False)

print("Data loaded into SQLite table 'weather' in weather.db")
conn.close()
