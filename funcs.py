

# import requests as req
import json
import os
import datetime
import bcrypt


CWD = os.path.dirname(__file__)

# url = 'https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json'

# res = req.get(url).json()

def menu():
    print('Welcome to DEA APP'.center(50, '-'))
    print('1. Users')
    print('2. Enter to DEA')
    print('3. Exit')

def submenu():
    print('1. Create a new user')
    print('2. Login')
    print('3. Back to main menu')

def submenu2():
    print('1. Search DEA by code')
    print('2. Search nearest DEA by location')
    print('3. Modify DEA by code')
    print('4. Back to main menu')

# def write_json():
#     with open(f'{CWD}/dea.json', 'w', encoding = 'utf8') as file:
#         json.dump(res, file, ensure_ascii = False, indent = 4)


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

def search_by_loc(db, h_user):
    result = []
    for dea in db:
        h = ((int(dea['direccion_coordenada_x']) ** 2) + (int(dea['direccion_coordenada_y']) ** 2)) * 0.5
        result.append(h)
    result2 = sorted(result, key = lambda h: h > h_user)
    return result2[0]

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

class Dea():
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    @property
    def search_by_loc(self):
        h = ((self.x ** 2) + (self.y ** 2)) * 0.5
        return h

des = Dea(325, 456)
result = des.search_by_loc
print(result)



