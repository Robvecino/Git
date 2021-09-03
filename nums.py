import random

def create_number():
    a = str(random.randint(1, 9))
    count_prima = 0
    while count_prima == 0:
        b = str(random.randint(1, 9))
        if a == b:
            count_prima = 0
        else:
            c = str(random.randint(1, 9))
            if c == a or c == b:
                count_prima = 0
            else:
                number = a + b + c
                return number

number = create_number()

def validate(num):
    if '0' in num:
        return False
    else:
        to_validate = [num for num in num]
        for i, digit in enumerate(to_validate):
            to_validate.remove(digit)
            if digit in to_validate:
                return False
            else:
                return True

print('Welcome to Nums The Game')
count = 0
history = {}
counter = 0
while count == 0:
    result = []
    count_val = 0
    while count_val == 0:
        user_num = input('Try to guess the number. Please, insert your choice: ')
        user_num_validation = validate(user_num)
        if user_num_validation == False:
            print('The choice is not valid. Please, try again.')
            count_val = 0
        else:
            count_val = 1

    # if number[0] == user_num[0]:
    #     result.append('1E')
    # elif number[0] == user_num[1]:
    #     result.append('1M')
    # elif number[0] == user_num[2]:
    #     result.append('1M')
    # else:
    #     pass

    # if number[1] == user_num[0]:
    #     result.append('1M')
    # elif number[1] == user_num[1]:
    #     result.append('1E')
    # elif number[1] == user_num[2]:
    #     result.append('1M')
    # else:
    #     pass

    # if number[2] == user_num[0]:
    #     result.append('1E')
    # elif number[2] == user_num[1]:
    #     result.append('1M')
    # elif number[2] == user_num[2]:
    #     result.append('1E')
    # else:
    #     pass

    # if len(result) == 0:
    #     result.append('No match')
    # print(f'This is your result: {result}')
    # history.update({user_num : result})
    # if result == ['1E', '1E', '1E']:
    #     print (f'You win in {counter + 1} attemp(s)')
    #     print(history)
    #     count = 1
    # else:
    #     print('Your choice is not correct. Please, try again!')
    #     print(history)
    #     counter += 1
    #     count = 0

#* Otra forma de realizar el ejercicio (mejor):

    counter_e = 0
    counter_m = 0
    for num in user_num:
        if num in number:
            if user_num.find(num) == number.find(num):
                counter_e += 1
            else:
                counter_m += 1
        else:
            continue
    if counter_e > 0:
        result.append(f'{counter_e}E')
    if counter_m > 0:
        result.append(f'{counter_m}M')
    if len(result) == 0:
        result.append('No match')
    print(f'This is your result: {result}')
    history.update({user_num : result})
    if result == ['3E']:
        print (f'You win in {counter + 1} attemp(s)')
        print(history)
        count = 1
    else:
        print('Your choice is not correct. Please, try again!')
        print(history)
        counter += 1
        count = 0
