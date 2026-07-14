import requests

API_KEY = "032896d8ea6fb84831f79aff472e347b"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:

        city_name = data["name"]
        country = data["sys"]["country"]

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        description = data["weather"][0]["description"]

        wind_speed = data["wind"]["speed"]

        print("\n===== WEATHER REPORT =====")
        print(f"City: {city_name}, {country}")
        print(f"Temperature: {temperature} °C")
        print(f"Feels Like: {feels_like} °C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.title()}")
        print(f"Wind Speed: {wind_speed} m/s")

    else:
       print("Status Code:", response.status_code)
       print(data)
        

except Exception as e:
    print("Error:", e)