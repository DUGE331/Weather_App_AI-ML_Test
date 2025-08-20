import requests
#import os

#api_key = os.environ.get('WEATHER_API')
api_key= "c25ab11e4f3d0bc80c022ea23b7efc86"

user_input =input("Enter your city: ")
weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("City not found, please try again.")
else:   
    weather= weather_data.json()['weather'][0]['main']
    temp= round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°C")
