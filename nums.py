import random

def create_number():
    a = str(random.randint(1,9))
    count_prima = 0
    while count_prima == 0:
        b = str(random.randint(1,9))
        if a == b:
            count_prima = 0
        else:
            c = str(random.randint(1,9))
            if c == a or c == b:
                count_prima = 0
            else:
                number = a + b + c
                return number

number = create_number()

print('Welcome to Nums The Game')
count = 0
history = {}
counter = 0
while count == 0:
    result = []
    user_num = input('Try to guess the number. Please, insert your choice: ')

    if number[0] == user_num[0]:
        result.append('1E')
    elif number[0] == user_num[1]:
        result.append('1M')
    elif number[0] == user_num[2]:
        result.append('1M')
    else:
        pass

    if number[1] == user_num[0]:
        result.append('1M')
    elif number[1] == user_num[1]:
        result.append('1E')
    elif number[1] == user_num[2]:
        result.append('1M')
    else:
        pass

    if number[2] == user_num[0]:
        result.append('1E')
    elif number[2] == user_num[1]:
        result.append('1M')
    elif number[2] == user_num[2]:
        result.append('1E')
    else:
        pass

    if len(result) == 0:
        result.append('No match')
    print(f'This is your result: {result}')
    history.update({user_num : result})
    if result == ['1E', '1E', '1E']:
        print (f'You win in {counter + 1} attemp(s)')
        print(history)
        count = 1
    else:
        print('Your choice is not correct. Please, try again!')
        print(history)
        counter += 1
        count = 0