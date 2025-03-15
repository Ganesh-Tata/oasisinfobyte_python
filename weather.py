#Basic wether app
import requests

def get_weather(api_key, location):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def display_weather(weather_data):
    try:
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_conditions = weather_data['weather'][0]['description']
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Conditions: {weather_conditions}")
    except KeyError:
        print("Error: Could not retrieve weather data.")

def main():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    location = input("Enter a city or ZIP code: ")
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
