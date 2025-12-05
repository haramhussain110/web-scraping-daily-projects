"""
Weather Finder App (Task 02)
--------------------------------
A simple Python script that finds the current temperature
of ANY city by using the free Open-Meteo API.

Author: Haram Hussain
"""

import requests

print("====================================")
print("      WEATHER DATA EXTRACTION        ")
print("====================================")

#  Taking city name from user 
city = input("Enter city name: ").strip()

try:
    print("\nFinding city location...")

    # Step 2: Get latitude + longitude from Geocoding API
    geo_url = (
        "https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}&count=1"
    )
    geo_response = requests.get(geo_url).json()

    # Check if city exists
    if not geo_response.get("results"):
        print("City not found. Try another name.")
    else:
        # Extract coordinates
        lat = geo_response["results"][0]["latitude"]
        lon = geo_response["results"][0]["longitude"]

        print(f"Location found → LAT: {lat}, LON: {lon}")
        print("Fetching live weather...\n")

        # Get current weather using coordinates
        weather_url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current_weather=true")

        weather_response = requests.get(weather_url).json()

        # Extract temperature
        temp = weather_response["current_weather"]["temperature"]
        wind = weather_response["current_weather"]["windspeed"]
        direction = weather_response["current_weather"]["winddirection"]

        #  Show result
        print(f"City: {city.title()}")
        print(f"Temperature: {temp}°C")
        print(f"Wind Speed: {wind} km/h")
        print(f"Wind Direction: {direction}°")

except Exception as error:
    print("Something went wrong:", error)
