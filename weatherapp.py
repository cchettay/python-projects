import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("WEATHER_API_KEY")

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    city + "&appid=" + API_KEY + "&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    name = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print("\n===== WEATHER =====")
    print("City      :", name + ",", country)
    print("Temperature  :", temp, "°C")
    print("Feels like   :", feels_like, "°C")
    print("Humidity     :", humidity, "%")
    print("Description  :", description)
else:
    print("City not found! Please check the name.")
```

---

**Step 4 — Push to GitHub: **
```
git add .
git commit - m "Fix exposed API key"
git push
