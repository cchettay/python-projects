import requests  # to talk to internet

# paste your API key here  to open the openweathermap
API_KEY = "b00a0b997346dc0a12414363a2f3d9ca"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    city + "&appid=" + API_KEY + "&units=metric"  # builds web address to send request

response = requests.get(url)  # ask qn to app and store answer in response
data = response.json()  # converts ans to dictionary

if data["cod"] == 200:  # check if req is succesfull 200 is successful and 404 is not successfull
    name = data["name"]  # get city name from dictionary
    country = data["sys"]["country"]  # get country code
    # Gets the temperature. Opens `data` box, opens `main` box, gets `temp`.
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    # select data from list.[0]  select first item
    description = data["weather"][0]["description"]

    print("\n===== WEATHER =====")
    print("City      :", name + ",", country)
    print("Temperature  :", temp, "°C")
    print("Feels like   :", feels_like, "°C")
    print("Humidity     :", humidity, "%")
    print("Description  :", description)
else:
    print("City not found! Please check the name.")
