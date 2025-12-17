import requests
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()  # loads variables from .env file
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("API key not found! Set OPENWEATHER_API_KEY environment variable.")

cities = ["London", "New York", "Tokyo"]
data = []

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        data.append({
            "city": json_data["name"],
            "timestamp": datetime.utcnow()
            "temperature_c": json_data["main"]["temp"],
            "humidity": json_data["main"]["humidity"],
            "description": json_data["weather"][0]["description"]
        })
    else:
        print(f"Failed for {city}: {response.status_code}")

df = pd.DataFrame(data)
output_file = "weather_data.csv"
df.to_csv(output_file, index=False)
print(f"Saved {len(df)} records to {output_file}")
