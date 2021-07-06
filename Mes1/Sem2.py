
# #!Ejercicios viernes
# #*Ejercicio 1
# students = ["Pedro", "Luís", "Milagros", "Marta", "Macarena", "Marcelo", "Epifanio"]
# #*Ejercicio 2
# students_copy = students.copy()
# print(students_copy)
# #* #Ejercicio 3
# print(len(students_copy))
# #* #Ejercicio 4
# Milagros = students_copy.index('Milagros')
# students_copy.pop(Milagros)
# print(students_copy)
# #*Otra forma
# #students_copy.remove('Milagros)
# #print(students_copy)
# # #* #Ejercicio 5
# Macarena = students_copy.index('Macarena')
# print(Macarena)
# # #* #Ejercicio 6
# students_copy.insert(len(students_copy) // 2, 'Germán')
# print(students_copy)
# # #* #Ejercicio 7
# new_students = ["Felipe", "Tomás", "Facundo"]
# students_copy.extend(new_students)
# print(students_copy)
# # *#Ejercicio 8
# students = students_copy.copy()
# print(students)

# #!Ejercicios while y operador in
# #*Ejercicio 1
# count = 0
# while count < len(students):
#     print(students[count].upper())
#     count += 1

# # #*Ejercicio 2
# count = 0
# while count < len(students):
#     print(students[count] + 'lo')
#     count += 1

# #*Ejercicio 3
# count = 0
# sumatorio = 0
# while count < len(students):
#     if 'M' in students[count]:
#         sumatorio += 1
#     count += 1
# print(sumatorio)

#*Otra forma
# count = 0
# resultado = 0
# while count < len(students):
#     if students[count].startswith('M'):
#         resultado += 1
#     count += 1
# print(resultado)

#*Otra forma
# count = 0
# resultado = 0
# while count < len(students):
#     if 'M' == students[count][0]:
#         resultado += 1
#     count += 1
# print(resultado)

# # #* #Ejercicio 4
# count = 0
# while count < len(students):
#     print(f'El estudiante {students[count]} ocupa el lugar {count}')
#     count += 1

#*Ejercicio 5
# approved_students = ["Pedro", "Felipe", "Macarena", "Epifanio"]

# count = 0
# while count < len(students):
#     if students[count] in approved_students:
#         print(f'El estudiante {students[count]} ha aprobado')
#     else:
#         print(f'El estudiante {students[count]} no ha aprobado')
#     count += 1

#*Ejercicio 6

# count = 0
# user = input('Introduzca un alumno: ')
# while count < len(students):
#     if user in students:
#         if user == students[count]:
#             print(count)
#             break
#         else:
#             count += 1

#*Otra forma

# user = input('Student search: ')
# count = 0
# while count < len(students):
#     if user in students:
#         print(f'El estudiante {user} se encuentra en la posición {count}')
#         count = len(students)
#     count += 1

# #*Ejercicio 7
# count = 0
# while count < len(students):
#     user_1 = input('Introduzca un alumno: ')
#     if user_1 in students:
#         user_2 = input('Introduzca un nombre: ')
#         students.remove(user_1)
#         students.append(user_2)
#         print(students)
#         count += 1
#     else:
#         print('No existen alumnos registrados con ese nombre.')
#     count += 1

#*Otra forma
# user = input('Students search: ')
# count = 0
# while count < len(students):
#     if user == students[count]:
#         students[count] = input('New name: ')
#         count == len(students) + 1

#     if count == len(students) - 1:
#         print(f'El estudiante {user} no se encuentra en la lista')
#     count += 1
# print(students)

# #*Ejercicio 8
# new_course = []
# count = 0
# while count < len(students):
#     user_1 = input('Introduzca un alumno: ')
#     if user_1 in students:
#         user_2 = input('¿Quiere introducir al alumno en el nuevo grupo?: ')
#         if user_2 == 'Sí':
#             new_course.append(user_1)
#             print(new_course)
#             count += 1
#         else:
#             count += 1


# #*Ejercicio 9
# new_course = []
# count = 0
# while count < len(students):
#     user_1 = input('Introduzca un alumno: ')
#     if user_1 in students:
#         new_course.append(user_1)
#         print('El alumno ha sido ingresado con éxito: ', new_course)
#         count += 1
#     else:
#         print('Este alumno no está registrado')
#         count += 1

#*Otra forma

# count= 0
# new_course = []
# user = input('Estudiante a buscar: ')
# while count < len(students):
#     if user == students[count]:
#         new_course.append(user)
#     count += 1
# print(new_course)

#!Explicaciones lunes

# numeros = [1,2,3,4]
# pares = []
# count = 0
# while count < len(numeros):
#     if numeros[0] % 2 == 0:
#         pares.append(numeros[count])
#     count += 1
# print(pares)

# print('Bienvenidos a Students App---')
# print('1. Buscar estudiante') #?Corresponde al ejercicio 6
# print('2. Buscar y actualizar estudiante') #?Corresponde al ejercicio 7
# print('3. Para salir')
# user = input('Elija opción: ')

# while user != '3':
#     if user == '1':
#         user = input('Estudiante a buscar: ')
#         count = 0
#         while count < len(students):
#             if user in students:
#                 print(f'El estudiante {user} se encuentra en la posición {count}')
#             count = len(students)
#             count += 1
#     user = input('Y ahora qué?: ')

# #!Ejercicios martes

# #*Ejercicio conversor
# print('---Converter APP---')
# user = '0'

# while user != '5':
#     print('1. Length converter')
#     print('2. Volume converter')
#     print('3. Mass converter')
#     print('4. Speed converter')
#     print('5. Exit')
#     user = input('Please choose an option: ')
#     if user == '1':
#         print('a. Kms to Mi')
#         print('b. Mts to In')
#         user = input('Choose a or b: ')
#         if user == 'a':
#             user = input('Insert data: ')
#             user = int(user) * 0.621371
#             print(f'Result: {user} Mi')
#             user = input('e for exit or m for menu: ')
#             if user == 'e':
#                 break
#             elif user == 'm':
#                 user = '0'
#         elif user == 'b':
#             user = input('Insert data: ')
#             user = int(user) * 39.370
#             print(f'Result: {user} In')
#             user = input('e for exit or m for menu: ')
#             if user == 'e':
#                 break
#             elif user == 'm':
#                 user = '0'
#     if user == '2':
#         print('a. Lt to Gal')
#         print('b. Gal to Lt')
#         user = input('Choose a or b: ')
#         if user == 'a':
#             user = input('Insert data: ')
#             user = int(user) * 0.26417
#             print(f'Result: {user} Gal')
#             user = input('e for exit or m for menu: ')
#             if user == 'e':
#                 break
#             elif user == 'm':
#                 user = '0'
#         elif user == 'b':
#             user = input('Insert data: ')
#             user = int(user) / 0.26417
#             print(f'Result: {user} Lt')
#             user = input('e for exit or m for menu: ')
#             if user == 'e':
#                 break
#             elif user == 'm':
#                 user = '0'
#         if user == '3':
#             user = input('Insert Kg data to convert into Lb: ')
#             user = int(user) * 2.2046
#             print(f'Result: {user} Lb')
#             user = input('e for exit or m for menu: ')
#             if user == 'e':
#                 break
#             elif user == 'm':
#                 user = '0'
#         if user == '4':
#             user = input('Insert M/s data to convert into Km/h: ')
#             user = int(user) * 1.7
#             print(f'Result: {user} Km/h')
#             user = input('e for exit or m for menu: ')
#             if user == 'e':
#                 break
#             elif user == 'm':
#                 user = '0'
# print('Thank you for using this app!')

# #*Otra forma

# print('---Converter APP---')
# count = 0
# while count < 1:
#     print('<<<<<Main menu>>>>>')
#     print('1. Length converter')
#     print('2. Volume converter')
#     print('3. Mass converter')
#     print('4. Speed converter')
#     print('5. Exit')
#     print('<<<<<>>>>>')
#     user = input('Please choose an option: ')
#     if user == '1':
#         print('a. Kms to Mi')
#         print('b. Mts to In')
#         user = input('Choose a or b: ')
#         if user == 'a':
#             user = input('Insert data: ')
#             user = int(user) * 0.621371
#             print(f'Result: {user} Mi')
#             user = input('e for exit or m for menu: ')
#             if user == 'e':
#                 count += 1
#             else:
#                 pass
#         elif user == 'b':
#             user = input('Insert data: ')
#             user = int(user) * 39.370
#             print(f'Result: {user} In')
#             user = input('e for exit or m for menu: ')
#             if user == 'e':
#                 count += 1
#             else:
#                 pass
#     if user == '2':
#         print('a. Lt to Gal')
#         print('b. Gal to Lt')
#         user = input('Choose a or b: ')
#         if user == 'a':
#             user = input('Insert data: ')
#             user = int(user) * 0.26417
#             print(f'Result: {user} Gal')
#             user = input('e for exit or m for menu: ')
#             if user == 'e':
#                 count += 1
#             else:
#                 pass
#         elif user == 'b':
#             user = input('Insert data: ')
#             user = int(user) / 0.26417
#             print(f'Result: {user} Lt')
#             user = input('e for exit or m for menu: ')
#             if user == 'e':
#                 count += 1
#             else:
#                 pass
#     if user == '3':
#         user = input('Insert Kg data to convert into Lb: ')
#         user = int(user) * 2.2046
#         print(f'Result: {user} Lb')
#         user = input('e for exit or m for menu: ')
#         if user == 'e':
#             count += 1
#         else:
#             pass
#     if user == '4':
#         user = input('Insert M/s data to convert into Km/h: ')
#         user = int(user) * 1.7
#         print(f'Result: {user} Km/h')
#         user = input('e for exit or m for menu: ')
#         if user == 'e':
#             count += 1
#         else:
#             pass
#     if user == '5':
#         count += 1
# print('Thank you for using this app!')

#!Ejercicios miércoles

#*Diccionarios

# test = {'name': 'Roberto', 'apellido': 'Vecino'}
# print(test['name'])
# #?Como claves valen variables, enteros, cadenas de string o tuplas, pero no listas.

# from typing_extensions import Unpack


book = {"id": "cf_1", "title": "El hombre bicentenario", "author": "Isaac Asimov", "genre": "Ciencia ficción"}
# print(book)
# book['author'] = 'Roberto Vecino'
# print(book)
# book_keys = book.keys()
# print(book_keys)
book_values = book.values()
# print(book_values)
# print(len(book))


# count = 0
# while count < len(book):
#     if count == 0:
#         print(book['id'])
#     count += 1
#     if count == 1:
#         print(book['title'])
#     count += 1
#     if count == 2:
#         print(book['author'])
#     count += 1
#     if count == 3:
#         print(book['genre'])
#     count += 1

# #*Otra forma
# book_list = list(book_values)
# count = 0
# while count < len(book_list):
#     print(book_list[count])
#     count += 1

#*Bucles for

# nums = [1,2,3,4]

# for sexys in nums:
#     print(sexys)

# string = 'Hola'

# for letra in string:
#     print(letra)

# for valor in book_values:
#     print(valor)
# book_items = list(book.items())

# for tupla in book_items:
#     print(tupla)

# for tupla in book_items:
#     print(tupla[1])

# for tupla in book_items:
#     print(f'El {tupla[0]} es {tupla[1]}')

# #*Otra forma

# for tupla in book_items:
#     clave = tupla[0]
#     valor = tupla[1]
#     print(f'El {clave} es {valor}')

#!Ejercicios jueves

bookshop = [{
    "id": "cf_1",
    "title": "El hombre bicentenario",
    "author": "Isaac Asimov",
    "genre": "Ciencia ficción"
},
{
    "id": "ne_1",
    "title": "Lobo de mar",
    "author": "Jack London",
    "genre": "Narrativa extranjera"
},
{
    "id": "np_1",
    "title": "El legado de los huesos",
    "author": "Dolores Redondo",
    "genre": "Narrativa policíaca"
},
{
    "id": "dc_1",
    "title": "El error de Descartes",
    "author": "Antonio Damasio",
    "genre": "Divulgación científica"
},
{
    "id": "dc_2",
    "title": "El ingenio de los pájaros",
    "author": "Jennifer Ackerman",
    "genre": "Divulgación científica"
},
{
    "id": "ne_1",
    "title": "El corazón de las tinieblas",
    "author": "Joseph Conrad",
    "genre": "Narrativa extranjera"
},
{
    "id": "dc_5",
    "title": "Metro 2033",
    "author": "Dmitri Glujovski",
    "genre": "Divulgación científica"
},
{
    "id": "dc_5",
    "title": "Sidharta",
    "author": "Hermann Hesse",
    "genre": "Narrativa extranjera"
},
{
    "id": "el_1",
    "title": "Andres Trapiello",
    "author": "Las armas y las letras",
    "genre": "Narrativa extranjera"
},
{
    "id": "aa_1",
    "title": "El poder del ahora",
    "author": "Ekhart Tolle",
    "genre": "Narrativa extranjera"
},
]

genres = ["Narrativa extranjera", "Divulgación científica", "Narrativa policíaca", "Ciencia ficción", "Autoayuda"]

# print(bookshop)

# for elements in bookshop:
#     print(elements)

# #*Otra forma

# count = 0

# while count < len(bookshop):
#     print(bookshop[count])
#     count += 1

# book_1 = bookshop[0]
# print(book_1['author'])

# #*Otra forma
# print(bookshop[0]['title'])

#?Ejercicio app diccionario

print('Search-o-matic APP'.center(50, "-"))
count = 0
while count < 1:
    print('Main menu'.center(50, '-'))
    print('1. Search for id'.center(15))
    print('2. Search for author'.center(15))
    print('3. Search for title'.center(15))
    print('4. Search for genre'.center(15))
    print('5. Create an entry'.center(15))
    print('6. Update an entry'.center(15))
    print('7. Delete an entry'.center(15))
    print('8. Exit'.center(15))
    print('###################')
    user = input('Please, choose an option: ')
    if user == '1':
        print('Welcome to Search-O-Matic id'.center(15))
        book_id = input('Insert an id: '.center(15))
        control = True
        for book in bookshop:
            if book['id'] == book_id:
                print('###########')
                print('This is your result: '.center(15))
                for k, v in book.items():
                    print(f'----\n{k} : {v}')
                    control = True
            else:
                control = False
        if control == False:
            print(f'Your search: {book_id} has no result.')
        print('###########')
        user = input('Where do you want to go now?\nPlease, insert "e" for exit or "m" for menu: ')
        if user == 'e':
            count += 1
        else:
            count = 0
    elif user == '2':
        print('Welcome to Search-O-Matic author'.center(15))
        book_author = input('Insert an author: '.center(15))
        control = 0
        for book in bookshop:
            user_author = book['author'].lower().find(book_author.lower())
            if user_author >= 0:
                print('###########')
                print('This is your result: '.center(15))
                for k, v in book.items():
                    print(f'----\n{k} : {v}')
                    control += 1
        if control == 0:
            print(f'Your search: {book_author} has no result.')
        print('###########')
        user = input('Where do you want to go now?\nPlease, insert "e" for exit or "m" for menu: ')
        if user == 'e':
            count += 1
        else:
            count = 0
    elif user == '3':
        print('Welcome to Search-O-Matic title'.center(15))
        book_title = input('Insert a title: '.center(15))
        control = 0
        for book in bookshop:
            user_title = book['title'].lower().find(book_title.lower())
            if user_title >= 0:
                print('###########')
                print('This is your result: '.center(15))
                for k, v in book.items():
                    print(f'----\n{k} : {v}')
                    control += 1
        if control == 0:
            print(f'Your search: {book_title} has no result. Please, try again.')
        print('###########')
        user = input('Where do you want to go now?\nPlease, insert "e" for exit or "m" for menu: ')
        if user == 'e':
            count += 1
        else:
            count = 0
    elif user == '4':
        print('Welcome to Search-O-Matic genre'.center(15))
        for i, gen in enumerate(genres):
            print(f'{i + 1}. {gen}')
        book_genre = int(input('Insert the number of the genre you want to search: '.center(15)))
        book_genre = genres[book_genre - 1]
        result = []
        print('###########')
        print('This is your result: '.center(15))
        for book in bookshop:
            if book['genre'] == book_genre:
                    result.append(book)
        count = 0
        print(f'---------{book_genre}--------')
        for books in result:
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
        user = input('Where do you want to go now?\nPlease, insert "e" for exit or "m" for menu: ')
        if user == 'e':
            count += 1
        else:
            count = 0
    elif user == '5':
        keys = list(bookshop[0].keys()) #*Claves genéricas
        newbook_id = 'nb_' + str(len(bookshop))
        new_book = {}
        new_book['id'] = newbook_id
        for k in keys[1:3]: #*Se crea un diccionario con las claves
            new_book[k] = input(f'{k}: ')
        for i, gen in enumerate(genres):
            print(f'{i + 1}. {gen}')
        newbook_genre = int(input('Insert the number of the genre you want to add: '.center(15)))
        newbook_genre = genres[newbook_genre - 1]
        new_book['genre'] = newbook_genre
        bookshop.append(new_book) #*Se incluye en la lista de libros
    elif user == '6':
        upd_id = input('Insert an id: '.center(15))
        control = True
        for book in bookshop:
            if book['id'] == upd_id:
                print('###########')
                print('This is your result: '.center(15))
                for i, t in enumerate(book.items()):
                    print(f'{i + 1}. {t[0]} : {t[1]}')
                    control = True
                user_upd = int(input('Insert the number of the part you want to update: ')) - 1
                keys = list(book.keys())
                upd_key = keys[user_upd]
                book[upd_key] = input(f'Insert the new data to change "{book[upd_key]}": ')
                print(f'The data was successfully updated to: {book[upd_key]}')
                print('This is the updated data: ')
                print('----------------')
                for k, v in book.items():
                    print(f'{k} : {v}')
            else:
                control = False
        if control == False:
            print(f'Your search: {book_id} has no result.')
        print('###########')
        user = input('Where do you want to go now?\nPlease, insert "e" for exit or "m" for menu: ')
        if user == 'e':
            count += 1
        else:
            count = 0
    elif user == '7':
        del_id = input('Insert an id to delete: ')
        control = True
        for book in bookshop:
            if book['id'] == del_id:
                print('###########')
                print('This is your search: '.center(15))
                for k, v in book.items():
                    print(f'----\n{k} : {v}')
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
        user = input('Where do you want to go now?\nPlease, insert "e" for exit or "m" for menu: ')
        if user == 'e':
            count += 1
        else:
            count = 0
    elif user == '8':
        count += 1
    else:
        print('This is not a valid option. Please, try again.')
        count = 0
print('Thank you for using this app!')