
import json
import os
import bcrypt
import datetime


CWD = os.path.dirname(__file__)

class Auth:
    def __init__(self, db_path):
        if type(db_path) != str:
            raise ValueError('The db_path must be an str instance')
        self.db_path = db_path
    
    @property
    def users(self):
        with open(self.db_path, 'r', encoding = 'utf8') as file:
            return json.load(file)['data']

    def create_user(self, user):
        if type(user) != dict:
            raise ValueError('The user has to be an dictionary instance')
        users = self.users.copy()
        users.append(user)
        with open(self.db_path, 'w', encoding = 'utf8') as file:
            json.dump({'data' : users}, file, ensure_ascii = False, indent = 4)

    @staticmethod
    def create_form():
        user_name = input('Name: ')
        user_pwd = input('Password: ')
        return {'user_name' : user_name, 'user_pwd' : user_pwd}
    
    @staticmethod
    def login_form():
        user_input = input('Insert a name: ')
        user_pwd = input('Insert a password: ').encode()
        password_hash = bcrypt.hashpw(user_pwd, bcrypt.gensalt())
        return {'user_name' : user_input, 'user_pwd' : user_pwd, 'pwd_hash' : password_hash}
    
    def login(self, login):
        if type(login) != dict:
            raise ValueError('The user has to be an dictionary instance')
        users = self.users.copy()
        valid_name = list(filter(lambda user: user['user_name'] == login['user_name'], users))
        if len(valid_name) > 0 and bcrypt.checkpw(login['user_pwd'], login['pwd_hash']):
            user_token = {'password' : login['pwd_hash'].decode() + login['user_name'], 'expire_date' : datetime.datetime.today()}
            print("Valid entry! Access granted") 
            return user_token
        else:
            print("Invalid entry! Access denied")

test = Auth(f'{CWD}/users.json')
test_user = test.create_form()
test.create_user(test_user)
log_form = test.login_form()
log = test.login(log_form)
