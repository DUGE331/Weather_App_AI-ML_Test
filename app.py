import requests
import os

api_key = os.environ.get('WEATHER_API')
api = c25ab11e4f3d0bc80c022ea23b7efc86

user_input =input("Enter your city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

print(weather_data.status_code)