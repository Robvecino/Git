import json
import csv
#! Ejercicios lunes
# genre = 'narrativa extranjera'
# print(genre.split(' '))

#! Ejercicios martes
#TODO Extensiones más comunes con las que se trabaja en Python: .csv y .json

#!Trabajar con archivos

#* Función «open» para abrir ficheros
# lorem = open('lorem.txt')
# print(lorem)
# print(lorem.read())
# data = lorem.read()
# print(data)
# print(data.split(' '))
# for word in data.split(' '):
#     print(word.upper())

#? El método «read» llega hasta el final y para que vuelva hay que utilizar el método «seek» y buscar la posición donde quiero que empiece a leer el cursor de «read».

#* Ejercicio 1
# lorem = open('lorem.txt')
# data = lorem.read().lower().replace('lorem', 'natura') #* En este caso, no hace falta usar «lower». Si hubiese más «lorem» con minúscula, habría que hacer un método «lower».
# print(data)
# lorem.close()

#* Abrir en modo lectura

# lorem = open('lorem.txt', 'r') #? Es redundante porque es el método por defecto si no le pasas nada

#* Abrir en modo escritura

# lorem = open('lorem.txt', 'w')

#TODO Si utilizamos el método write directamente en la variable, la reescribe por completo.

# lorem.write(data)

#* Ejercicio 2

# read_lorem = open('lorem.txt')
# data = read_lorem.read()
# data = data.replace('Lorem', 'Natura')
# write_lorem = open('lorem.txt', 'w')
# write_lorem.write(data)
# write_lorem.close()
# read_lorem.close()

# #* Palabra «with»

# with open('lorem.txt') as lorem: #? Dentro de la indentación de «with» hay oculto, al final, un .close().
#     print(lorem.read())

# with open('lorem.txt') as lorem:
#     data = lorem.read()
#     data = data.replace('Lorem', 'Natura')
#     with open('lorem.txt', 'w') as lorem:
#         lorem.write(data)

# print(data)
# longitud = len(data) #TODO Podemos trabajar con las variables creadas dentro de «with» aunque se cierre el archivo con el que hemos trabajado.

# #! Ejercicios miércoles

# lorem = open('./lorem.txt') #* El punto y la barra es para que Python busque el lugar exacto donde se encuentre el archivo sin tener que estar situado en su carpeta.

# #? Para fusionar dos txt

# with open('lorem.txt') as lorem:
#     lorem_txt = lorem.read()

# with open('lorem2.txt') as lorem2:
#     lorem2 = lorem2.read()
#     lorem_new = lorem_txt + ' ' + lorem2

# with open('lorem.txt', 'w') as lorem:
#     lorem.write(lorem_new)

# #TODO Trabajar con .json

# with open('bookshop.json') as file:
#     print(file.read())

# with open('bookshop.json', encoding = 'utf8') as file:
#     data = json.load(file)
#     print(data['books'][-1])

# with open('bookshop.json', encoding = 'utf8') as file:
#     data = json.load(file)
#     new_book = {
#     "id": "np_77",
#     "title": "El legado de los huesos",
#     "author": "Dolores Redondo",
#     "genre": "Narrativa policíaca"
# }
#     data['books'].append(new_book)
#     print(data)

# with open('bookshop.json', 'w', encoding = 'utf8') as file:
#     json.dump(data, file, ensure_ascii = False) #* Con ensure_ascii nos aseguramos que los datos se van a mostrar en el json sin ascii.



# #? Introducimos la librería «json» para importar el método «load» y pasar los datos del json a un diccionario.de Python. Además, agregamos el encoding UTF-8 para que se vean bien los caracteres.

# #! Ejercicios jueves
# def write_json(what, where):
#     with open(where, 'w', encoding = 'utf8') as file:
#         json.dump(what, file, ensure_ascii = False, indent = 4)

# #TODO Para pasar strings a Python hay que usar los métodos con «s»
# objectJS = '"name" : rober'
# dict_python = json.load(objectJS)

# from_dict = json.dumps(dict_python)
# print(type(from_dict))

#* Trabajar con .csv

with open('export_bookshop.csv', encoding = 'utf8') as file:
    print(file.readlines()) #? Para leer el archivo

with open('export_bookshop.csv', 'w', encoding = 'utf8', newline = '') as file:
    csv_writer = csv.writer(file, delimiter = ',') #? «Newline» y «delimiter» sirven para que Windows no meta filas vacías entre las filas que agreguemos al csv.
    csv_writer.writerow(['Hola']) #TODO Si no se mete el str en una lista, lo itera por cada carácter y te los separa cada uno por comillas.