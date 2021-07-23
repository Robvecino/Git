
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
        elif user == '2':
            data = funcs.open_json_user()
            user_token = funcs.login(data)
            server_token = user_token
            smcount = funcs.submenu_end(count)
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
        elif user == '2':
            data = funcs.open_json()
            x_user = int(input('Insert your X location: '))
            y_user = int(input('Insert your Y location: '))
            h_user = Dea(x_user, y_user)
            user_result = h_user.search_by_loc
            h_data = funcs.search_by_loc(data)

            sm2count = funcs.submenu_end(count)
                        
        elif user == '3':
            data = funcs.open_json()
            # if user_token:
            #     if (user_token['expire_date']  + datetime.timedelta(minutes = 30)) > datetime.datetime.today():
            #         if user_token == server_token:

            #     else:
            #         print('Your session has already expired. Please, login again')
            # else:
            #     print('You are not loged. Please, login to access.')
            sm2count = funcs.submenu_end(count)
        elif user == '4':
            sm2count += 1
        else:
            print('Invalid input!')
            smcount = 0

