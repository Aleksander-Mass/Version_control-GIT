import requests
import pprint

DOMAIN = 'https://api.hh.ru/'

url_vacancies = f'{DOMAIN}vacancies'

params = {
    'text': 'C# developer',
#     # страница
    'page': 1
}

result = requests.get(url_vacancies, params=params)

print(result.status_code)

pprint.pprint(result.json())
