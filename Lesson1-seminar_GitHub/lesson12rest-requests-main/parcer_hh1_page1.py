import requests
import pprint

DOMAIN = 'https://api.hh.ru/'

url_vacancies = f'{DOMAIN}vacancies'

params = {
    'text': 'C# developer',
    #     # страница
    'page': 1
}

result = requests.get(url_vacancies, params=params).json()

items = result['items']

first = items[0]

#pprint.pprint(first)

print(first['alternate_url'])
print(first['url'])
