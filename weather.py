import requests


def main():
    url_sunfrancisco = 'https://wttr.in/sun%20francisco'
    variable_london = 'Лондон'
    variable_moscov_airport_sheremetivo = 'SVO'
    variable_cherepovec = 'Череповец'
    charcteristic_windows = {
        'lang': 'ru',
        'n': '',
        'q': '',
        'T':'',
        'M':''
    }
    weather_cherepovec = f'https://wttr.in/{variable_cherepovec}'
    weather_sheremetivo = f'https://wttr.in/{variable_moscov_airport_sheremetivo}'
    weather_london = f'https://wttr.in/{variable_london}'
    response_cherepovec = requests.get(weather_cherepovec, params=charcteristic_windows)
    response_sheremetivo = requests.get(weather_sheremetivo, params=charcteristic_windows)
    response_london = requests.get(weather_london, params=charcteristic_windows)
    response_cherepovec.raise_for_status()
    print(response_cherepovec.text)
    response_sheremetivo.raise_for_status()
    print(response_sheremetivo.text)
    response_london.raise_for_status()
    print(response_london.text)


if __name__ == '__main__':
    main()