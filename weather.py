import requests


def create_url(city):
    return f'https://wttr.in/{city}'


def get_weather(parametrs, func):
    response = requests.get(func, params=parametrs)
    #response.raise_for_status()
    return response


def main():
    cities = ['Лондон', 'SVO', 'Череповец']

    charcteristic_windows = {
        'lang': 'ru',
        'n': '',
        'q': '',
        'T': '',
        'M': '',
    }

    for city in cities:
        url_city = create_url(city)
        weather_in_city = get_weather(charcteristic_windows, url_city)
        print(weather_in_city.text)


if __name__ == '__main__':
    main()