
import json
import os

CWD = os.path.dirname(__file__)
def menu():
    print('1. Create user')
    print('2. Login')
    print('3. Exit')

def new_user():
    user_dict = {}
    user_input = input('Insert a name: ')
    user_pwd = input('Insert a password: ')
    user_dict['name'] = user_input
    user_dict['pwd'] = user_pwd
    return user_dict


def write_json(dic):
    with open(f'{CWD}/users.json', 'w', encoding = 'utf8') as file:
        json.dump({'users' : [dic]}, file, ensure_ascii = False, indent = 4)

def open_json():
    with open(f'{CWD}/users.json', 'r+', encoding = 'utf8') as file:
        data = json.load(file)['users']
        file.seek(0)
    return data

def append_json(new_data):
    with open(f'{CWD}/users.json', 'r+', encoding = 'utf8') as file:
        data = json.load(file)
        data["users"].append(new_data)
        file.seek(0)
        json.dump(data, file, ensure_ascii = False, indent = 4)


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
