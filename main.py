import json
from json.decoder import JSONDecodeError
import funcs
import datetime

server_token = None
user_token = None
count = 0

while count < 1:
    funcs.menu()
    user = input('Choose an option: ')
    if user == '1':
        try:
            data = funcs.open_json()
            new_user = funcs.new_user()
            for user in data:
                if new_user['name'] == user['name']:
                    new_user['name'] = input('This name has already been used. Please, select another: ')
            funcs.append_json(new_user)
        except JSONDecodeError:
            new_user = funcs.new_user()
            funcs.write_json(new_user)
        count = funcs.submenu_end(count)
    elif user == '2':
        data = funcs.open_json()
        user_token = funcs.login(data)
        server_token = user_token
        count = funcs.submenu_end(count)
    elif user == '3':
        data = funcs.open_json()
        if user_token:
            if (user_token['expire_date']  + datetime.timedelta(minutes = 1)) > datetime.datetime.today():
                if user_token == server_token:
                    funcs.change_pwd(data)
            else:
                print('Your session has already expired. Please, login again')
        else:
            print('You are not loged. Please, login to access.')
        count = funcs.submenu_end(count)
    elif user == '4':
        count += 1
