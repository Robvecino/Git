
# import requests as req
import json
import os
import datetime
import bcrypt
import utm

CWD = os.path.dirname(__file__)

# url = 'https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json'

# res = req.get(url).json()

def menu():
    print('Welcome to DEA APP'.center(50, '-'))
    print('1. Users')
    print('2. Enter to DEA')
    print('3. Coordinates conversor')
    print('4. Exit')

def submenu():
    print('1. Create a new user')
    print('2. Login')
    print('3. Back to main menu')

def submenu2():
    print('1. Search DEA by code')
    print('2. Search nearest DEA by location')
    print('3. Update DEA by code')
    print('4. Search 10 nearest DEAs by location')
    print('5. Back to main menu')

# def write_json():
#     with open(f'{CWD}/dea.json', 'w', encoding = 'utf8') as file:
#         json.dump(res, file, ensure_ascii = False, indent = 4)

# write_json()

def open_json():
    with open(f'{CWD}/dea.json', encoding = 'utf8') as file:
        data = json.load(file)['data']
    return data

def open_json_user():
    with open(f'{CWD}/users.json', encoding = 'utf8') as file:
        data = json.load(file)['users']
    return data


# data = open_json()
# print(len(data))

# list_cp = ['28029', '28036', '28046', '28039', '28016', '28020', '28002', '28003', '28015', '28010', '28006', '28028', '28008', '28004', '28001', '280013', '28014', '28009', '28007', '28012', '28005', '28045']

# count = 0

# for dea in data:
#     if dea['direccion_codigo_postal'] in list_cp:
#         count += 1

# print(count)

# search2 = list(filter(lambda dea: dea['tipo_titularidad'] == 'Pública', data))
# search3 = list(filter(lambda dea: dea['tipo_titularidad'] == 'Privada', data))
# print(len(search2))
# print(len(search3))

def write_json_users(dic):
    with open(f'{CWD}/users.json', 'w', encoding = 'utf8') as file:
        json.dump({'users' : [dic]}, file, ensure_ascii = False, indent = 4)

def new_user():
    user_dict = {}
    user_input = input('Insert a name: ')
    user_pwd = input('Insert a password: ').encode()
    password_hash = bcrypt.hashpw(user_pwd, bcrypt.gensalt())
    final_pwd = password_hash.decode()
    user_dict['name'] = user_input
    user_dict['pwd'] = final_pwd
    user_dict['user_since'] = datetime.date.today().isoformat()
    print('New user successfully created!')
    return user_dict

def append_json(new_data):
    with open(f'{CWD}/users.json', 'r+', encoding = 'utf8') as file:
        data = json.load(file)
        data["users"].append(new_data)
        file.seek(0)
        json.dump(data, file, ensure_ascii = False, indent = 4)

def login(db):
    user_input = input('Insert a name: ')
    user_pwd = input('Insert a password: ').encode()
    password_hash = bcrypt.hashpw(user_pwd, bcrypt.gensalt())
    valid_name = list(filter(lambda user: user['name'] == user_input, db))
    if len(valid_name) > 0 and bcrypt.checkpw(user_pwd, password_hash):
        user_token = {'password' : password_hash.decode() + user_input, 'expire_date' : datetime.datetime.today()}
        print("Valid entry! Access granted") 
        return user_token
    else:
        print("Invalid entry! Access denied")

def search_by_code(user_input, db):
    for dea in db:
        if dea['codigo_dea'] == user_input:
            print(dea)

def search_by_code2(user_input, db):
    for dea in db:
        if dea['codigo_dea'] == user_input:
            return dea

class Dea():
    def __init__(self, x ,y):
        if type(x) != int:
            raise Exception('Only inter input')
        if type(y) != int:
            raise Exception('Only inter input')
        self.x = x
        self.y = y

    def search_by_loc(self, user_x, user_y):
        c_1 = (self.x - user_x) ** 2
        c_2 = (self.y - user_y) ** 2
        h = (c_1 + c_2) ** 0.5
        return h

def search_by_loc(db, x_user, y_user):
    distance_beat = 999999999999
    first_place = None
    count = 0
    for dea in db:
        dea_obj = Dea(int(dea['direccion_coordenada_x']), int(dea['direccion_coordenada_y']))
        distance = dea_obj.search_by_loc(x_user, y_user)
        if distance <= distance_beat:
            first_place = dea
            distance_beat = distance
    return first_place

def search_by_loc2(db, x_user, y_user):
    count = 0
    for dea in db:
        dea_obj = Dea(int(dea['direccion_coordenada_x']), int(dea['direccion_coordenada_y']))
        distance = dea_obj.search_by_loc(x_user, y_user)
        dea['distance'] = distance
        count += 1
    result = list(sorted(db, key = lambda dea: dea['distance']))[0:11]
    print('The nearest 10 DEAs are:')
    for dea in result:
        print(f'{dea["direccion_ubicacion"]}')

def index_dea(iterable):
    for i, v in enumerate(iterable):
        print(f'{i + 1}. {v}')

def print_DEA(dea):
    for k, v in dea.items():
        print(f'-------\n{k} : {v}')

def upd_DEA(user_dea, db):
    if user_dea != None:
        keys = list(user_dea)
        index_dea(keys)
        try:
            user_upd = int(input('Insert the number of the part you want to update: ')) - 1
        except ValueError:
            print('Invalid entry!')
            return None
        upd_key = keys[user_upd]
        db.remove(user_dea)
        user_dea[upd_key] = input(f'Insert the new data to change "{user_dea[upd_key]}": ')
        db.append(user_dea)
        print(f'The data was successfully updated to: {user_dea[upd_key]}')
        print('This is the updated data: ')
        print('----------------')
        print_DEA(user_dea)
        return db
    else:
        print('Invalid entry!')
        return None

def overwrite_json_users(data):
    with open(f'{CWD}/dea.json', 'w', encoding = 'utf8') as file:
        json.dump({'data' : data}, file, ensure_ascii = False, indent = 4)

def coordinates_conv():
    user_choice = input('Insert "U" if you want to convert to utm or "L" to convert to lat/lon: ')
    if user_choice.lower() == 'u':
        try:
            user_lat = float(input('Insert the latitude: '))
        except ValueError:
            print('Invalid input!')
            return None
        try:
            user_lon = float(input('Insert the longitude: '))
        except ValueError:
            print('Invalid input!')
            return None
        print(f'This is your result: {utm.from_latlon(user_lat, user_lon)}')
    elif user_choice.lower() == 'l':
        try:
            user_x = float(input('Insert the x input: '))
        except ValueError:
            print('Invalid input!')
            return None
        try:
            user_y = float(input('Insert the y input: '))
        except ValueError:
            print('Invalid input!')
            return None
        print(f'This is your result: {utm.to_latlon(user_x, user_y)}')
    else:
        print('Invalid input!')
        return None

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



