import requests


def main():
    url_sunfrancisco = 'https://wttr.in/sun%20francisco'
    variable_london = 'Лондон'
    variable_moscov_airport_sheremetivo = 'SVO'
    variable_cherepovec = 'Череповец'
    url_template = f'https://wttr.in/{variable_cherepovec}?lang=ru&?n&?q&?T&?M'
    response = requests.get(url_template)
    response.raise_for_status()

    return response.text


if __name__ == '__main__':
    print(main())