import requests as req
import json
import csv
from languages import languages
import os
from collections import Counter
real_path = os.path.dirname(__file__)

def menu():
    print('Welcome to Country Search App'.center(50, '-'))
    print('Main menu'.center(50, '-'))
    print('1. Search by country'.center(15))
    print('2. Search by continent'.center(15))
    print('3. Search country by language'.center(15))
    print('4. Search and download flag'.center(15))
    print('5. Record')
    print('6. Exit')
    print('###################')

def read_csv():
    with open('export_countries.csv', encoding = 'utf8') as file:
        csv_read = csv.reader(file, delimiter = ';')
        next(csv_read)
        result = [line for line in csv_read]
        return result

def record():
    lines = read_csv()
    for line in lines:
        if line[0] != 'Name':
            print(f'name: {line[0]} - population: {line[3]}')

def get_country(name):
    res = req.get(f'https://restcountries.eu/rest/v2/name/{name}').json()
    if type(res) != list:
        print(f'The country: {name}, has no result')
    elif res[0]['name'].lower() == name:
        return [res[0]['name'], res[0]['capital'], res[0]['region'], res[0]['population'], res[0]['area'], res[0]['languages'][0]['name'], res[0]['flag']]
    elif res[0]['name'].lower().find(name.lower()) >= 0:
        return [res[0]['name'], res[0]['capital'], res[0]['region'], res[0]['population'], res[0]['area'], res[0]['languages'][0]['name'], res[0]['flag']]

def get_country_flag(name):
    res = req.get(f'https://restcountries.eu/rest/v2/name/{name}').json()
    if type(res) != list:
        print(f'The country: {name}, has no result')
    elif res[0]['name'].lower() == name:
        return res[0]['flag']
    elif res[0]['name'].lower().find(name.lower()) >= 0:
        return res[0]['flag']

def down_flag(user_flag, user_entry):
    res = req.get(f'{user_flag}').content
    with open(f'{real_path}/images/{user_entry}.svg', 'wb') as file:
        file.write(res)
    

def get_region(region):
    res = req.get(f'https://restcountries.eu/rest/v2/region/{region}').json()
    if type(res) != list:
        print(f'The continent: {region}, has no result')
    else:
        return res

def get_country_by_lan(lang):
    res = req.get(f'https://restcountries.eu/rest/v2/lang/{lang}').json()
    if type(res) != list:
        print(f'The language: {lang}, has no result')
    else:
        lang = list(map(lambda country: country['name'], res))
        return (lang)

def submenu_end(count):  
        user = input('Where do you want to go now?\nPlease, insert "e" for exit or "m" for menu: ')
        if user.lower() == 'e':
            count = 1
            return count
        elif user.lower() == 'm':
            count = 0
            return count
        else:
            print('Invalid input. Returning back to the main menu...')
            count = 0
            return count

def write_csv(user_input):
    with open('export_countries.csv', 'a', encoding = 'utf8', newline = '') as file:
        csv_writer = csv.writer(file, delimiter = ';', dialect = 'excel')
        csv_writer.writerow(user_input)

def write_json(user_input, continent):
    with open(f'{real_path}/{user_input}.json', 'w', encoding = 'utf8') as file:
        data = json.dump({'data': continent}, file, ensure_ascii = False, indent = 4)
    return data
    
def open_json(user_region):
    with open(f'{real_path}/{user_region}.json', encoding = 'utf8') as file:
        continent = json.load(file)['data']
    return continent

def get_population(continent):
    result = 0
    for country in continent:
        result += country['population']
    return result

def get_population2(db):
    population = list(map(lambda country: country['population'], db))
    return sum(population)

def get_iso(language):
    result = list(filter(lambda tupla: tupla[1].lower().find(language) == 0, languages))
    if len(result) == 0:
        print(f'The language: {language}, has no result')
    else:
        return result[0][0]

def get_10_area():
    res = req.get('https://restcountries.eu/rest/v2/all').json()
    resultado = sorted(res, key = lambda country: country['area'] if type(country['area']) == float else 0, reverse = True)
    return resultado[0:11]

# result = get_10_area()

# for i, country in enumerate(result):
#     print(f'{i + 1}. {country["name"]}')

def get_10_den():
    res = req.get('https://restcountries.eu/rest/v2/all').json()
    resultado = sorted(res, key = lambda country: country['population'], reverse = True)
    return resultado[0:11]

# result = get_10_den()

# for i, country in enumerate(result):
#     print(f'{i + 1}. {country["name"]}')

def get_lang1():
    resultado = []
    res = req.get('https://restcountries.eu/rest/v2/all').json()
    for country in res:
        resultado.append(country['languages'][0]['name'])
    return resultado

# languages = get_lang1()

# print(Counter(languages).most_common()[0][0])

#? Otras formas (con los ISO):

def get_lang2():
    result = {}
    res = req.get('https://restcountries.eu/rest/v2/all').json()
    languages = [country['languages'][0]['iso639_1'] for country in res]
    u_languages = set([[country['languages'][0]['iso639_1'] for country in res]])
    for u_language in u_languages:
        result[u_language] = languages.count(u_language)
    return dict(sorted(result.items(), key = lambda tupla: tupla[1], reverse = True))

def get_lang3():
    result ={}
    res = req.get('https://restcountries.eu/rest/v2/all').json()
    for country in res:
        language = country['languages'][0]['name']
        try:
            result[language] += 1
        except KeyError:
            result[language] = 1
    return dict(sorted(result.items(), key = lambda tupla: tupla[1], reverse = True))




