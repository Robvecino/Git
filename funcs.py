
import json
import os

CWD = os.path.dirname(__file__)
def menu():
    print('1. Create user')
    print('2. Login')


def new_user(db):
    user_dict = {}
    user_input = input('Insert a name: ')
    user_pwd = input('Insert a password: ')
    user_dict['name'] = user_input
    user_dict['pwd'] = user_pwd
    db.append(user_dict)
    return db

def write_json(db):
    with open(f'{CWD}/users.json', 'w', encoding = 'utf8') as file:
        json.dump({'users' : db}, file, ensure_ascii = False, indent = 4)

def open_json():
    with open(f'{CWD}/users.json', encoding = 'utf8') as file:
        data = json.load(file)['users']
    return data

# def upd_json(db):
#     with open(f'{CWD}/users.json', 'a', encoding = 'utf8') as file:
#         json.dump(db, file['users'], ensure_ascii = False, indent = 4)
