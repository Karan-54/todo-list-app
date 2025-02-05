import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "units": "metric",
        "appid": api_key
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data

def print_weather(weather_data):
    if "name" in weather_data:
        print(f"\nWeather in {weather_data['name']}:")
        print(f"Description: {weather_data.get('weather', [{}])[0].get('description', 'N/A')}")
        print(f"Temperature: {weather_data.get('main', {}).get('temp', 'N/A')}°C")
        print(f"Feels like: {weather_data.get('main', {}).get('feels_like', 'N/A')}°C")
        print(f"Humidity: {weather_data.get('main', {}).get('humidity', 'N/A')}%")
        print(f"Wind speed: {weather_data.get('wind', {}).get('speed', 'N/A')} m/s")
    else:
        print("\n⚠️ Error: Unexpected API response format!")
        print("Raw Response:", weather_data)  # Debugging: Shows the full response from the API

def main():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your actual API key
    location = input("Enter city name: ")
    weather_data = get_weather(api_key, location)

    if weather_data.get("cod") == 200:  # Ensure successful response
        print_weather(weather_data)
    elif weather_data.get("cod") == "404":
        print("\n❌ City not found. Please check the spelling and try again.")
    else:
        print("\n⚠️ API Error:", weather_data.get("message", "Unknown error occurred."))

if __name__ == "__main__":
    main()
