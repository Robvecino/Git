import json
import csv
# #!Ejercicios lunes

# #*Función enumerate
# a = [1,2,3,4]
# for i, nums in enumerate(a):
#     print(f'{i +1}. {nums}')

# #!Ejercicios miércoles

# a = [1,2,3,4] #*Se guarda un valor.
# print(a)
# a.append(5)
# a.pop(0)

# #*Crear funciones
# def name_of_func():
#     print('lo que quieras que suceda')

# for num in a:
#     print(a)

# name_of_func() #*Se guarda una acción.

# def saludar():
#     print('HOLA!')

# def saludar_a(name): #?Lo que va entre paréntesis es el o los parámetros de la función que hemos creado. Podemos poner los parámetros quq queramos y llamarlos como queramos, siempre y cuando no utilicemos palabras reservadas.
#     print(f'Hola {name}')

# saludar_a('Rober')
# saludar_a('Manu')

# def potencia(num):
#     num = num**2
#     print(num)

# potencia(4)

# #! Ejercicios jueves

# #? Existen variables a nivel global, como la variable «a» de arriba, así como variables a nivel local que existen solo dentro de las funciones que creamos.

# def doble(numero):
#     result = numero **2
#     print(result)

# doble(7)

# def listado(lista): #TODO Así es mejor crear funciones. Se recomienda utilizar parámetros neutros, para, después, usar la variable que queramos.
#     for num in lista:
#         print(num)

# listado(a)

# def ordenar(lista):
#     lista.sort()
#     return lista #TODO Al introducir «return», podemos trabajar cualquier lista que le pasemos por parámetro (en el ejemplo, la lista ordenada).

# lista_ordenada = ordenar(a)
# print(a)
# print(lista_ordenada)
# lista_ordenada.append(10)

# #! Ejercicio 1

# def saludos():
#     print('Buen día!')

# def saludo_personal(name):
#     print(f'Buen día, {name}!')

# def al_cuadrado(num):
#     print(num**2)

# def al_cubo(num):
#     num = num**3
#     return num

# saludos()

# saludo_personal('Rober')

# al_cuadrado(5)

# resultado = al_cubo(5)
# print(resultado)


# #! Continuación ejercicos jueves

# def suma(num_1, num_2): #? Las funciones pueden recibir «n» parámetros.
#     print(num_1 + num_2)

# suma(4, 3)

with open('./bookshop.json', encoding = 'utf8') as file:
    bookshop = json.load(file)['books']

genres = ["Narrativa extranjera", "Divulgación científica", "Narrativa policíaca", "Ciencia ficción", "Autoayuda"]

def menu():
    print('Main menu'.center(50, '-'))
    print('1. Search for id'.center(15))
    print('2. Search for author'.center(15))
    print('3. Search for title'.center(15))
    print('4. Search for genre'.center(15))
    print('5. Create an entry'.center(15))
    print('6. Update an entry'.center(15))
    print('7. Delete an entry'.center(15))
    print('8. Import to Excel'.center(15))
    print('9. Exit'.center(15))
    print('###################')

def get_id(id, db):
    control = True
    for book in db:
        if book['id'] == id:
            control = True
            return book
        else:
            control = False
    if control == False:
        print(f'Your search: {id} has no result.')

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


def get_title_author(user_input, db, key):
        control = 0
        result = []
        for book in db:
            if book[key].lower().find(user_input.lower()) >= 0:
                result.append(book)
                control += 1
        if control == 0:
            print(f'Your search: {user_input} has no result. Please, try again.')
        return result

def get_genres(user_input, db, list):
    user_input = list[user_input - 1]
    result = []
    print('###########')
    print('This is your result: '.center(15))
    for book in db:
        if book['genre'] == user_input:
            result.append(book)
    return result

def print_genres(user_input,book_input, list):
    count = 0
    print(f'---------{list[book_input - 1]}--------')
    for books in user_input:
        print(f'----Libro{count + 1}----')
        print(books['id'])
        print(books['author'])
        print(books['title'])
        print(books['genre'])
        count += 1
    if count == 0:
        print(f'No results found')
    if count == 1:
        print(f'1 book has been found')
    print(f'The number of results was {count}')
    print('###########')

def new_input(user_input):
    keys = list(bookshop[0].keys())
    new_book = {}
    new_book['id'] = user_input
    for k in keys[1:3]:
        new_book[k] = input(f'{k}: ')
    return new_book

def print_new_input(user_input, list, db, user_book):
        user_input = list[user_input - 1]
        user_book['genre'] = user_input
        db.append(user_book)
        print('Input successfully created!')
        print('###########')

def indice(lista):
    for i, v in enumerate(lista):
        print(f'{i + 1}. {v}')

def print_book(book):
    for k, v in book.items():
        print(f'-------\n{k} : {v}')

def write_json():
    with open('./bookshop.json', 'w', encoding = 'utf8') as file:
        json.dump({'books': bookshop}, file, ensure_ascii = False, indent = 4)

def write_csv():
    with open('export_bookshop.csv', 'w', encoding = 'utf8', newline = '') as file:
        csv_writer = csv.writer(file, delimiter = ',', dialect = 'excel')
        csv_writer.writerow(list(bookshop[0].keys()))
        for book in bookshop:
            csv_writer.writerow(book.values())


print('Search-o-matic APP'.center(50, "-"))
count = 0
while count < 1:
    menu()
    user = input('Please, choose an option: ')
    if user == '1':
        print('Welcome to Search-O-Matic id'.center(15))
        book_id = input('Insert an id: '.center(15))
        user_id = get_id(book_id, bookshop)
        if user_id != None:
            print_book(user_id)
        print('###########')
        count = submenu_end(count)
    elif user == '2':
        print('Welcome to Search-O-Matic author'.center(15))
        key = 'author'
        book_author = input('Insert an author: '.center(15))
        user_author = get_title_author(book_author, bookshop, key)
        for book in user_author:
            print_book(book)
        print('###########')
        count = submenu_end(count)
    elif user == '3':
        print('Welcome to Search-O-Matic title'.center(15))
        key = 'title'
        book_title = input('Insert a title: '.center(15))
        user_title = get_title_author(book_title, bookshop, key)
        for book in user_title:
            print_book(book)
        print('###########')
        count = submenu_end(count)
    elif user == '4':
        print('Welcome to Search-O-Matic genre'.center(15))
        indice(genres)
        book_genre = int(input('Insert the number of the genre you want to search: '.center(15)))
        user_genre = get_genres(book_genre, bookshop, genres)
        print_genres(user_genre, book_genre, genres)
        count = submenu_end(count)
    elif user == '5':
        newbook_id = 'nb_' + str(len(bookshop))
        user_newbook = new_input(newbook_id)
        indice(genres)
        newbook_genre = int(input('Insert the number of the genre you want to add: '.center(15)))
        print_new_input(newbook_genre, genres, bookshop, user_newbook)
        write_json()
        count = submenu_end(count)
    elif user == '6':
        upd_id = input('Insert an id: '.center(15))
        book_upd = get_id(upd_id, bookshop)
        if book_upd != None:
            keys = list(book_upd)
            indice(keys)
            user_upd = int(input('Insert the number of the part you want to update: ')) - 1
            upd_key = keys[user_upd]
            bookshop.remove(book_upd)
            book_upd[upd_key] = input(f'Insert the new data to change "{book_upd[upd_key]}": ')
            bookshop.append(book_upd)
            print(f'The data was successfully updated to: {book_upd[upd_key]}')
            print('This is the updated data: ')
            print('----------------')
            print_book(book_upd)
            write_json()
            count = submenu_end(count)
        else:
            print('Not a valid id')
            count = submenu_end(count)
    elif user == '7':
        del_id = input('Insert an id to delete: ')
        control = True
        for book in bookshop:
            if book['id'] == del_id:
                print('###########')
                print('This is your search: '.center(15))
                print_book(book)
                confirm_del = input(f'Do you really want to delete "{book["title"]}"? \nInsert "y" to confirm or "n" to cancel: ')
                if confirm_del == 'y':
                    bookshop.remove(book)
                    print ('Sucessfully deleted!')
                    control = True
                elif confirm_del == 'n':
                    print('You have cancel the delete process.')
                    control = True
                else:
                    print('Invalid entry!')
                    control = True
            else:
                control = False
        if control == False:
            print(f'Your search: {del_id} has no result.')
        print('###########')
        write_json()
        count = submenu_end(count)
    elif user == '8':
        confirm_exp = input('Do you want to export the database to .csv file?\nInsert "y" to confirm or "n" to cancel: ')
        if confirm_exp == 'y':
            write_csv()
            print('Sucessfully exported!')
        elif confirm_exp == 'n':
            print('You have cancel the export process.')
        else:
            print('Invalid entry!')
        print('###########')
        count = submenu_end(count)
    elif user == '9':
        count += 1
    else:
        print('This is not a valid option. Please, try again.')
        count = 0
print('Thank you for using this app!')