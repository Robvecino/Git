import json
import funcs

count = 0

database = []

while count < 1:
    funcs.menu()
    user = input('Choose an option: ')
    if user == '1':
        try:
            json = funcs.open_json()
            new_user = funcs.new_user(database)
            json.append(new_user)
        except:
            new_user = funcs.new_user(database)
            funcs.write_json(new_user)