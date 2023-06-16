import requests as r
from dataclasses import dataclass

@dataclass
class Weather:
    temp: list
    forecast: list


def get_weather(url) -> Weather:
    request: r.Response = r.get(url=url)
    data: dict = request.json()
    temp = data['properties']['periods'][0]['temperature']
    forecast = data['properties']['periods'][0]['detailedForecast']
    return Weather(temp, forecast)


if __name__ == '__main__':

    url = 'https://api.weather.gov/gridpoints/GSP/105,58/forecast'

    weather: Weather = get_weather(url)

    print('Current temperature: ', weather.temp)
    print(weather.forecast)