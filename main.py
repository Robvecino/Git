import json
import funcs

count = 0

while count < 1:
    funcs.menu()
    user = input('Choose an option: ')
    if user == '1':
        try:
            json = funcs.open_json()
            new_user = funcs.new_user()
            for user in json:
                if new_user['name'] == user['name']:
                    new_user['name'] = input('This name has already been used. Please, select another: ')
            funcs.append_json(new_user)
        except:
            new_user = funcs.new_user()
            funcs.write_json(new_user)
        count = funcs.submenu_end(count)
    elif user == '3':
        count += 1
