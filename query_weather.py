import sqlite3
import pandas as pd

conn = sqlite3.connect("weather.db")

print("Query 1: All weather records")
df1 = pd.read_sql("SELECT * FROM weather;", conn)
print(df1)

print("\n🌡️ Query 2: Average temperature across cities")
df2 = pd.read_sql("""
    SELECT 
        AVG(temperature_c) as avg_temp,
        AVG(humidity) as avg_humidity
    FROM weather;
""", conn)
print(df2)

print("\nQuery 3: Rank cities by temperature (using ROW_NUMBER)")
df3 = pd.read_sql("""
    SELECT 
        city,
        temperature_c,
        ROW_NUMBER() OVER (ORDER BY temperature_c DESC) as temp_rank
    FROM weather;
""", conn)
print(df3)

conn.close()
