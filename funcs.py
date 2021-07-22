
import json
import os
import datetime
import bcrypt

CWD = os.path.dirname(__file__)
def menu():
    print('1. Create user')
    print('2. Login')
    print('3. Change password')
    print('4. Exit')

def new_user():
    user_dict = {}
    user_input = input('Insert a name: ')
    user_pwd = input('Insert a password: ').encode()
    password_hash = bcrypt.hashpw(user_pwd, bcrypt.gensalt())
    final_pwd = password_hash.decode()
    user_dict['name'] = user_input
    user_dict['pwd'] = final_pwd
    user_dict['user_since'] = datetime.date.today().isoformat()
    return user_dict

def change_pwd(db):
    user_input = input('Insert your name: ')
    user_pwd1 = input('Insert a new password: ').encode()
    user_pwd2 = input('Insert the new password again: ').encode()
    if user_pwd1 == user_pwd2:
        password_hash = bcrypt.hashpw(user_pwd2, bcrypt.gensalt())
        final_pwd = password_hash.decode()
        for client in db:
            if user_input == client['name']:
                client['pwd'] == final_pwd
                print('Your password has been successfully changed!')
            else:
                print('You are not registred')
    else:
        print('The new passwords did not match')

def write_json(dic):
    with open(f'{CWD}/users.json', 'w', encoding = 'utf8') as file:
        json.dump({'users' : [dic]}, file, ensure_ascii = False, indent = 4)

def open_json():
    with open(f'{CWD}/users.json', encoding = 'utf8') as file:
        data = json.load(file)['users']
    return data

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
