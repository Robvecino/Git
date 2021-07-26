import json
import funcs
import datetime

server_token = None
user_token = None
count = 0

while count < 1:
    funcs.menu()
    user = input('Choose an option: ')
    if user == '1':
        smcount = 0
        funcs.submenu()
        user = input('Choose an option: ')
        if user == '1':
            try:
                data = funcs.open_json_user()
                new_user = funcs.new_user()
                for user in data:
                    if new_user['name'] == user['name']:
                        new_user['name'] = input('This name has already been used. Please, select another: ')
                funcs.append_json(new_user)
            except FileNotFoundError:
                new_user = funcs.new_user()
                funcs.write_json_users(new_user)
            smcount = funcs.submenu_end(count)
            if smcount == 1:
                count = 1
        elif user == '2':
            data = funcs.open_json_user()
            user_token = funcs.login(data)
            server_token = user_token
            smcount = funcs.submenu_end(count)
            if smcount == 1:
                count = 1
        elif user == '3':
            smcount += 1
        else:
            print('Invalid input!')
            smcount = 0
    elif user == '2':
        sm2count = 0
        funcs.submenu2()
        user = input('Choose an option: ')
        if user == '1':
            data = funcs.open_json()
            user = input('Insert a DEA code to search: ')
            funcs.search_by_code(user, data)
            sm2count = funcs.submenu_end(count)
            if sm2count == 1:
                count = 1
        elif user == '2':
            data = funcs.open_json()
            x_user = int(input('Insert your X location: '))
            y_user = int(input('Insert your Y location: '))
            h_data = funcs.search_by_loc(data, x_user, y_user)
            sm2count = funcs.submenu_end(count)
            if sm2count == 1:
                count = 1
        elif user == '3':
            data = funcs.open_json()
            if user_token:
                if (user_token['expire_date']  + datetime.timedelta(minutes = 30)) > datetime.datetime.today():
                    if user_token == server_token:
                            user_input = input('Enter the code from the DEA to change: ')
                            user_dea = funcs.search_by_code2(user_input, data)
                            data_upd = funcs.change_DEA(user_dea, data)
                            funcs.overwrite_json_users(data_upd)
                else:
                    print('Your session has already expired. Please, login again')
            else:
                print('You are not loged. Please, login to access.')
            sm2count = funcs.submenu_end(count)
            if sm2count == 1:
                count = 1
        elif user == '4':
            data = funcs.open_json()
            x_user = int(input('Insert your X location: '))
            y_user = int(input('Insert your Y location: '))
            h_data = funcs.search_by_loc2(data, x_user, y_user)
            sm2count = funcs.submenu_end(count)
            if sm2count == 1:
                count = 1
        elif user == '5':
            sm2count += 1
        else:
            print('Invalid entry!')
            sm2count = 0
    elif user == '3':
        count += 1
    else:
        print('Invalid input!')
        count = 0


