
import requests as req
import func
#! Ejercicios viernes, lunes

# res = req.get('https://restcountries.eu/rest/v2/all').json()
# print(len(res))

#! Ejercicio App Country

count = 0
while count < 1:
    func.menu()
    user = input('Please, choose an option: ')
    if user == '1':
        print('Welcome to search by country'.center(15))
        user_entry = input('Insert the name of a country: '.center(15))
        user_country = func.get_country(user_entry)
        if type(user_country) == list:
            print(user_country)
            func.write_csv(user_country)
        count = func.submenu_end(count)
    elif user == '2':
        print('Welcome to search by continent'.center(15))
        user_entry = input('Insert the name of a continent (Asia, Europe, Americas, Oceania or Africa): '.center(15)).lower()
        try:
            continent = func.open_json(user_entry)
            population = func.get_population2(continent)
            print(f'The total population of {user_entry} is: {population} people')
        except FileNotFoundError:
            user_continent = func.get_region(user_entry)
            if type(user_continent) == list:
                data = func.write_json(user_entry, user_continent)
                # population = func.get_population(continent)
                # print(population)
                continent = func.open_json(user_entry)
                population = func.get_population2(continent)
                print(f'The total population of {user_entry} is: {population} people')
        count = func.submenu_end(count)
    elif user == '3':
        print('Welcome to search country by language'.center(15))
        user_entry = input('Insert a language: '.center(15))
        user_iso_entry = func.get_iso(user_entry)
        user_lang = func.get_country_by_lan(user_iso_entry)
        if type(user_lang) == list:
            print(f'This is your result: {user_lang}')
        count = func.submenu_end(count)
    elif user == '4':
        print('Welcome to search and download flag'.center(15))
        user_entry = input('Insert a country to download the flag: '.center(15))
        user_flag = func.get_country_flag(user_entry)
        if type(user_flag) == str:
            down_flag = func.down_flag(user_flag, user_entry)
            print('Successfully downloaded!')
        count = func.submenu_end(count)
    elif user == '5':
        print('Welcome to search record\nThis is the current record of searchs: '.center(15))
        read_csv = func.read_csv()
        func.record()
        count = func.submenu_end(count)
    elif user == '6':
        count += 1
    else:
        print('This is not a valid option. Please, try again.')
        count = 0
print('Thank you for using this app!')

#? Con «import os» y, luego os.path.dirname(__file__), lo metemos en una variable y lo podemos pasar como ruta al esribir un archivo y así, trabajar con una ruta absoluta y no relativa.

#! Ejercicios martes

#* Para descargar una imagen:

#? Importamos request y atacamos la url de la imagen y ponemos «.content» para descargar el contenido de la imagen. Después, usamos with open:

# res = req.get('la dirección de la imagen').content

# with open('img.svg', 'wb') as file:
#     file.write(res)

#* Manejo de errores:

# a = [1, 2, 3, 4]

# #TODO Escribimos «try», para que pruebe algo. A continuación, añadimos «except» para que, en caso de que no funcione, haga algo con ello. De esta manera, nos aseguramos que nuestro programa continúe. Se especifica el tipo de error que queramos manejar. Asimismo, se pueden agregar todos los «excepts» que queramos

# # try:
# #     print(a[4])
# except IndexError:
#     print('Algo no has hecho bien')

#! Ejercicios miércoles

#* Generadores (next):

# a = [1, 2, 3, 4]
# b = map(lambda num: num ** 2, a) #? «b» es un iterator. Si le añadimos la función «next», va haciendo iteración por iteración.
# print(next(b))

# #* Compresiones listas:

# a = [1, 2, 3, 4]

# for elemento in a:
#     elemento

# reslutado = [elemento for elemento in a] #TODO En las listas de compresión, su resultado permanece porque se puede guardar en variables.

# map(lambda elemento: elemento, a)

# filter(lambda elemento: elemento, a)

#* Operadores ternarios:
#? Es como un condicional con «if, else»

# valor = 'algún valor'

# resultado = True if condition else False

# b = 3

# #? Esto es un condicional con «if» normal:
# if b == 3:
#     print(True)
# else:
#     print(False)

# #? Esto es lo mismo, pero con operadores ternarios:
# print(True) if b == 3 else print(False)

# #TODO Se pueden concatenar los «if, else» que queramos.
# b = 101
# print('Es mayor que 100') if b > 100 else print('Es menor que 100') if b > 50 else print('Es menor a 50') if b > 10 else print('Es menor que 10')

#? Se puede meter un condicional dentro de una lista de compresión:

# reslutado = [elemento for elemento in a if elemento % 2 == 0] #* Para que nos devuelva los números pares.

#? Esto mismo hecho con operadores ternarios es:

# resultado = ['par' if elemento % 2 == 0 else 'impar' for elemento in a]



