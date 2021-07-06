import requests as req
import json
import statistics
#! Ejercicios viernes

#* Sintaxis avanzada

# a = [1,2,3,4]

# for value in a:
#     print(value)

#TODO Para reducir código a una línea podemos hacer una compresión de lista:

# result = []
# for value in a:
#     result.append(value**2)
# print(result)

# result = [value**2 for value in a]
# print(result)

#! Ejercicios lunes

#* Trabajar con la librería «requests» para trabajar con datos de internet. Primero, la hemos instalado en el cmd. Después, la importamos y la llamamos «req».
# url = 'https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/301aed82-339b-4005-ab20-06db41ee7017/download/municipio_comunidad_madrid.json'
# response = req.get(url).json() #? Get porque solicitamos información a la web; «json» porque queremos que nos pase la información en un .json.
# print(response)
# print(response['data'][0])
#TODO Ahora usamos la librería «json» para crear un .json propio donde metamos la info de la web:

# with open('./municipalities.json', 'w', encoding = 'utf8') as file:
#     json.dump(response, file, indent = 4, ensure_ascii = False)
#* Ahora, cargamos el json en una variable para poder trabajas sobre él.
def get_data():
    with open('./municipalities.json', encoding = 'utf8') as file:
        data = json.load(file)['data']
        return data

data = get_data()

#* Ejercicios con los datos extraídos de la web.

# def get_by_ine(ine, db):
#     for mun in db:
#         if mun['municipio_codigo_ine'] == ine:
#             return mun['municipio_nombre']

# test = get_by_ine('280029', data)
# print(test)

# #? Otra forma (con función «filter» y «lambda» dentro de la función).

# def get_by_ine2(ine, db):
#     resultado = list(filter(lambda mun: mun['municipio_codigo_ine'] == ine, db))
#     if len(resultado) == 1:
#         return resultado[0]['municipio_nombre']
#     else:
#         None

# test_2 = get_by_ine2('280029', data)
# print(test_2)

# def get_biggest(db):
#     resultado = []
#     for mun in db:
#         resultado.append(mun['superficie_km2'])
#     return max(resultado)

# print(get_biggest(data))

#? Otra forma

# def get_biggest2(db):
#     biggest = db[0]
#     for mun in db:
#         if mun['superficie_km2'] > biggest['superficie_km2']:
#             biggest = mun
#     return biggest['superficie_km2']

# big = get_biggest2(data)
# print(big)

# def superficie(db):
#     resultado = 0
#     for mun in db:
#         resultado = resultado + (mun['superficie_km2'])
#     return resultado

# print(superficie(data))

#? Otra forma (con la función «map»):

# def superficie2(db):
#     resultado = 0
#     superficies = list(map(lambda mun: resultado + mun['superficie_km2'], data))
#     return sum(superficies)

# area_total = superficie2(data)
# print(area_total)

# #? Otra forma (con compresión de lista):
# def superficie3(db):
#     return sum([mun['superficie_km2'] for mun in db])

# area_total = superficie3(data)
# print(area_total)

# def densidad(db):
#     resultado = 0
#     for mun in db:
#         resultado = resultado + (mun['densidad_por_km2'])
#     return resultado

# print(densidad(data))

# def poblacion(db):
#     resultado = 0
#     for mun in db:
#         resultado = resultado + (mun['superficie_km2']) * (mun['densidad_por_km2'])
#     return resultado

# print(int(poblacion(data)))

#? Otra forma (con a función «map»):
# def poblacion2(db):
#     densidades = list(map(lambda mun: mun['superficie_km2'], db))
#     superficies = list(map(lambda mun: mun['densidad_por_km2'], db))
#     resultado = list(map(lambda den, sup: den * sup, densidades, superficies))
#     return sum(resultado)

# test_pob = poblacion2(data)
# print(test_pob)


# def media_poblacion(db):
#     resultado = []
#     for mun in db:
#         suma = mun['superficie_km2'] * (mun['densidad_por_km2'])
#         resultado.append(suma)
#     return statistics.mean(resultado)

# print(media_poblacion(data))

# #? Otra forma
# print(int(poblacion(data)) / len(data))

# def benford(db):
#     list_1 = []
#     list_2 = []
#     list_3 = []
#     for mun in db:
#         if str(mun['densidad_por_km2']).startswith('1'):
#             list_1.append(mun)
#         elif str(mun['densidad_por_km2']).startswith('2'):
#             list_2.append(mun)
#         elif str(mun['densidad_por_km2']).startswith('3'):
#             list_3.append(mun)
#     res_1 = len(list_1) / len(data)
#     res_2 = len(list_2) / len(data)
#     res_3 = len(list_3) / len(data)
#     list_res = []
#     list_res.append(res_1)
#     list_res.append(res_2)
#     list_res.append(res_3)
#     return list_res

# print(benford(data))

# def benford2(db):
#     result = {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}
#     for mun in db:
#         result[str(mun['densidad_por_km2'])[0]] += 1
#     return result

# ben_2 = benford2(data)
# print([mun / len(data) for mun in ben_2.values()])

# def mas_grandes(db):
#     resultado = sorted(db, key = lambda mun: mun['superficie_km2'], reverse = True)
#     return resultado[0:11]

# test = mas_grandes(data)
# print(test)

# #? Otra forma (rara):
# def mas_grandes2(db):
#     result = []
#     for num in db:
#         result.append(max(db))
#         data.remove(max(db))
#     return result

#! Ejercicios miércoles

#* Otra forma

# def benford3(db):
#     proportion = 1 / len(db)
#     result = {}
#     for num in range(1,10):
#         result[str(num)] = 0
#     for mun in db:
#         result[str(mun['densidad_por_km2'])[0]] += proportion
#     return result

# ben_3 = benford3(data)
# print(ben_3)

#* Funciones avanzadas: funciones «lambda»

#? Funciones normales operan de la siguiente manera:

# def add(a, b):
#     return a + b

# print(add(3, 4))

#TODO Las funciones «lambda» operan así:

# funcion_lambda = lambda a, b: a + b #? Las funciones lambda se guarda en variables para poder operar con ellas
# result = funcion_lambda(3, 4)
# print(result)

# calculator = {'add' : lambda a, b: a + b, 'substract' : lambda a, b: a - b, 'times' : lambda a, b: a * b}
# print(calculator['substract'](3, 4))

#* Functional programming building-tools

#? Función «map»

#* Así opera una función normal (para elevar al cuadrado los números de la lista «a»):

# a = [1,2,3,4]

# def squares(lista):
#     result = []
#     for num in lista:
#         result.append(num ** 2)
#     return result

# print(squares(a))

# #* Así opera la función «map» (para elevar al cuadrado los números de la lista «a»):

# map_result = list(map(lambda num: num ** 2 , a))

# print(map_result)

# #? Función «filter» (para obtener los números pares de la lista «a»):

# filter_result = list(filter(lambda num: num % 2 == 0, a))

# print(filter_result)

#* Ejercicio 1

# a = [10, 123, 3, 2, 53, 345, 2, 1, 625, 3, 1, 4, 1, 50, 1, 65, 60]

# resultado = list(map(lambda num: num / 2, a))
# print(resultado)

#* Ejercicio 2

# a = [10, 123, 3, 2, 53, 345, 2, 1, 625, 3, 1, 4, 1, 50, 1, 65, 60]

# resultado = list(filter(lambda num: num % 2 != 0, a))
# print(resultado)

#! Ejercicios jueves

#* Función «next»

# a = [10, 123, 3, 2, 53, 345, 2, 1, 625, 3, 1, 4, 1, 50, 1, 65, 60]

# resultado = (filter(lambda num: num % 2 != 0, a))
# print(next(resultado))
# print(next(resultado))
# print(next(resultado))
# print(next(resultado))
# print(next(resultado))
# print(next(resultado))

#TODO Las funciones generadoras no guarnan nada en memoria. Una vez que aparecen por pantalla, no vuleven a aparecer. Si lo metemos en una lista, una tupla o un set, no se pierden los resultados de estas funciones.

# resultado = list(filter(lambda num: num % 2 != 0, a))

# #* Más ejemplos del uso de la función «map»:
# x = [10, 12, 20, 30, 41]
# y = [1, 3, 6, 7, 9]

# def merge_x_y():
#     result = []
#     for i, num in enumerate(x):
#         result.append(num * y[i])
#     return result

# resultado = merge_x_y()
# print(resultado)

# merge_x_y_map = list(map(lambda num_x, num_y: num_x * num_y, x, y))
# print(merge_x_y_map)

# data = {'superficie' : 10, 'superficie' :  3, 'superficie' : 7, 'superficie' : 11}
# a = [1, 3, 2, 4]

# a.sort() #TODO Destructiva
# sorted(a) #TODO No destructiva
# sorted(a, reverse = True)
# sorted(a, key = lambda num: num > 2) #? En este caso, «key» no está actuando y la lista se ordena de manera ascendente por defecto.
# sorted(data.values())
# dict(sorted(data.items(), key = lambda tupla: tupla[1]))

#* Cómo ordenar una lista:

data = [{'superficie' : 10}, {'superficie' :  3}, {'superficie' : 7}, {'superficie' : 11}]

sorted(data, key = lambda sup: sup['superficie'])

