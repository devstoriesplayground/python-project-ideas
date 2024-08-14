import requests
from tabulate import tabulate


def main():
    print("WELCOME TO DEVSTORIES PLAYGROUND - WEATHER APP")
    API_KEY = "d9bb3082731d46c59a472709241408" # Create your own API KEY once this one is
    try:
        user_input = input('Choose your city/region: ')
        url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={user_input}"
        response_data = requests.post(url)

        name = response_data.json()["location"]["name"]
        region = response_data.json()["location"]["region"]
        country = response_data.json()["location"]["country"]
        weather = response_data.json()["forecast"]["forecastday"][0]["day"]["condition"]["text"]
        temperature_c = round(response_data.json()["current"]["temp_c"], 2)
        temperature_f = round(response_data.json()["current"]["temp_f"], 2)

        print("Name:", name)
        print("City/Region:", region)
        print("Country:", country)
        print("Weather Condition:", weather)
        print("Temperature Celsius:", temperature_c, "celsius")
        print("Temperature Fahrenheit :", temperature_f, "fahrenheit")
    except Exception as ex:
        print(f"Error encountered -- {ex}")


if __name__ == "__main__":
    main()