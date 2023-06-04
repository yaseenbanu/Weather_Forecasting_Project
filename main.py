from weather_report import GetWeather
from dotenv import load_dotenv
import os
import requests
from colorama import init, Fore
from table import table
from data_formatter import format

if __name__ == '__main__':
    init(autoreset=True)
    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    units = ['standard', 'metric', 'imperial']

    try:
        unit_index = int(input('''Pick a unit of measurement
        1. Standard (Kelvin)
        2. Metric (Celsius)
        3. Imperial (Fahrenheit)
Enter your choice: '''))

        if unit_index != 1 and unit_index != 2 and unit_index != 3:
            raise Exception(f'{Fore.RED}Please enter an appropriate number')

        option = int(input('''Pick an option
        1. Search with City name
        2. Search with City and Country name
Enter your choice: '''))

        if option != 1 and option != 2:
            raise Exception(f'{Fore.RED}Please enter an appropriate number')

    except ValueError as ve:
        print(f'{Fore.RED}Please enter an integer')
        exit()

    try:
        app = GetWeather(API_KEY=API_KEY, unit=units[unit_index-1])
        data = None
        city = input('Enter City Name: ')

        if option == 1:
            data = app.get_weather_1(city=city)
        else:
            country = input('Enter Country Name: ')
            data = app.get_weather_2(city=city, country=country)

    except requests.ConnectionError as rce:
        print(f'{Fore.RED}Please connect to the Internet')
        exit()

    except requests.Timeout as rte:
        print(f'{Fore.RED}Request timedout')
        exit()

    except KeyError as ke:
        print(f'{Fore.RED}Please check the country name')
        exit()

    except IndexError as ie:
        print(f'{Fore.RED}Please check the city name')
        exit()

    except requests.exceptions.HTTPError as err:
        print(f'{Fore.RED}HTTP ERROR')
        raise SystemExit(err)

    except Exception as e:
        print(f'{Fore.RED}Terminated due the following reason')
        print(e)
        exit()

    required_data = format(data['main'], unit=units[unit_index])

    table(required_data)
