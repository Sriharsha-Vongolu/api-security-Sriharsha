
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError(
        "Missing OPENWEATHER_API_KEY. Add it to your .env file."
    )

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            print("Weather fetched successfully.")
            print("City:", data.get("name"))
            print("Temperature:", data.get("main", {}).get("temp"), "°C")
            print("Condition:", data.get("weather", [{}])[0].get("description"))
            return data

        elif response.status_code == 401:
            print("Error: Invalid or unauthorized API key.")
            return None

        elif response.status_code == 404:
            print("Error: City not found.")
            return None

        elif response.status_code == 429:
            print("Error: Rate limit exceeded. Please wait and try again later.")
            return None

        else:
            print(f"Error: API request failed with status code {response.status_code}")
            try:
                print("Response:", response.json())
            except ValueError:
                print("Response:", response.text)
            return None

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None


if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    get_weather(city)