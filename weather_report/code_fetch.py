import json
import requests
from weather_report.data_processing import etl


class GetWeather:

    def __init__(self, API_KEY, unit) -> None:
        self.__API_KEY = API_KEY
        self.unit = unit
        self.__coordinates_url = 'http://api.openweathermap.org/geo/1.0/direct'
        self.__weather_url = 'https://api.openweathermap.org/data/2.5/weather'

    def __fetch_cache(self) -> dict:
        try:
            with open("weather_report/data/cache.json", "r") as infile:
                return json.loads(infile.read())

        except FileNotFoundError as fnfe:
            etl()
            with open("weather_report/data/cache.json", "r") as infile:
                return json.loads(infile.read())

    def __fetch_code(self, country_name: str) -> str:
        cache = self.__fetch_cache()
        return cache[country_name.casefold()]

    def __fetch_geo_coordinates(self, city_name: str, country_code: str) -> dict:
        response = requests.get(
            f'{self.__coordinates_url}?q={city_name},{country_code}&limit={1}&appid={self.__API_KEY}')
        response.raise_for_status()
        data = response.json()[0]
        coordinates = {'lat': data['lat'], 'lon': data['lon']}
        return coordinates

    def __fetch_weather_data_1(self, city: str) -> dict:

        url = f'{self.__weather_url}?q={city}&appid={self.__API_KEY}&units={self.unit}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data

    def __fetch_weather_data_2(self, coordinates: dict) -> dict:
        lat = coordinates['lat']
        lon = coordinates['lon']
        url = f'{self.__weather_url}?lat={lat}&lon={lon}&appid={self.__API_KEY}&units={self.unit}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data

    def get_weather_1(self, city: str):
        weather_report = self.__fetch_weather_data_1(city=city)
        return weather_report

    def get_weather_2(self, city: str, country: str):
        country_code = self.__fetch_code(country_name=country)
        coordinates = self.__fetch_geo_coordinates(
            city_name=city, country_code=country_code)
        weather_report = self.__fetch_weather_data_2(coordinates=coordinates)
        return weather_report
