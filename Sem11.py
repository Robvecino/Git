
import threading
import time
import concurrent.futures
import os
import requests as req
CWD = os.path.dirname(__file__)
#! Clase lunes 06/09

#* Concurrencia (con la librería «Threading»)

# def a_dormir():
#     time.sleep(1) #? Esta función retrasa el funcionamiento de Python los segundos que le digamos. Se puede poner «secs» como parámetro.

# t_1 = threading.Thread(target = a_dormir)
# t_2 = threading.Thread(target = a_dormir) #* Aquí, se crean los «hilos» que ejecutan la función. Si ponemos «secs», hay que pasar, después del «target», args = [los segundos que queramos].

# t_1.start()
# t_2.start()#? Al ejecutar los hilos, se fuerza a Python a trabajar de manera asíncrona, por lo que la función que retrasa el funcionamiento tarda menos de los 2 sgundos que debería llevar la ejecución de la función «a dormir» dos veces seguidas.
# t_1.join()
# t_2.join() #? En este momento, la ejecuciónde Python vuelve al compertamiento por defecto y espera que se acabe la primera ejecucion de la función para, posteriormente, que se ejecute la segunda ejecución de la función. No obstante, como se ejecutaron a la vez de forma asíncrona, Python va a tardar 1 segundo en esperar a que los dos terminen, en vez de 2 segundos.

# #* Concurrencia (con la librería «Concurrent»)

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f_1 = executor.submit(a_dormir)#? De la misma forma que con la librería anterior, en esta línea se crea el hilo y se inicia en la misma línea, sin tener que iniciarlo en otra línea. Si ponemos «secs», hay que pasar, después de la función, los segundos que queramos para la función.
#     print(f_1.result()) #? En esta línea, simplemente se imprime cuánto ha tardado en ejecutarse la función del hilo.

#TODO Práctica de concurrencia
def get_flag(flag, i):
    res = req.get(flag).content
    with open(f'{CWD}/flags/{i}.svg', 'wb') as file:
        file.write(res)


# start = time.perf_counter()

# res = req.get('https://restcountries.eu/rest/v2/all').json()
# flags = []
# for country in res:
#     flags.append(country['flag'])

# for i, flag in enumerate(flags):
#     get_flag(flag, i)

# finish = time.perf_counter()
# print(finish - start)


start = time.perf_counter()

res = req.get('https://restcountries.eu/rest/v2/all').json()
flags = []
for country in res:
    flags.append(country['flag'])

for i, flag in enumerate(flags):
    t_1 = threading.Thread(target = get_flag, args = [flag, i])
    t_1.start()

finish = time.perf_counter()

print(finish - start)

#! Clase martes 07/09

#* Decoradores

#? De la siguienta manera, podemos meter en una variable («a») lo que retorna una función que se encuentra dentro de otra.
def container():
    print('I am inside')
    def n():
        print('n')
    return n()

a = container()
print(a)

#! Clase miércoles 08/09

# def funcion(*args): #? Al pasar «*args», decimos que a la función se le puede pasar múltiples argumentos.
#     for value in args:
#         print(value)

# def container(a_func):
#     def substract(*args):
#         pre_result1 = ''
#         for num in str(args[1]):
#             difference = range(int(num), 9)
#             pre_result1 = pre_result1 + str(len(difference))
#         pre_result1 = int(pre_result1)
#         pre_result2 = a_func(args[0], pre_result1)
#         pre_result2 = str(pre_result2)
#         pre_result3 = pre_result2[1:]
#         result = int(pre_result3) + 1
#         return result
#     return substract

# @container #? Aquí, escribimos el decorador; es decir, el nombre de la función contenedora.
# def add(a, b):
#     return a + b
# #? En el caso actual, nuestro decorador permite que se pueda pasar una función externa a la función «substract».
# print(add(121, 120))

#* Otro ejemplo de un decorador(para llevar un registro del uso de funciones y los argumentos utilizados en cada caso):

def write_in_log(external_func):
    def inner(*args):
        with open('funcs_recorder.log', 'a') as file:
            file.write(f'{external_func.__name__} func has been used with at least this arguments: {args}\n')
        return external_func(*args)
    return inner

@write_in_log
def add2(a, b):
    return a + b

@write_in_log
def substract2(a, b):
    return a - b

print(add2(1, 3))
print(substract2(1, 3))

#! Clase jueves 09/09

def ordenar(*args, **kwargs): #? Con «**kwargs», podemos pasar un diccionario entero como argumento.
    try:
        if kwargs['reverse']:
            print('Ordenar descendente')
    except KeyError:
        print('Ordenar ascendente')

ordenar(reverse = True)

#* Django

#? Es un framework para hacer páginas web con Python. Su estructura es muy rígida, lo cual hace difícil comprender su funcionamiento al principio.

#TODO La explicación continúa en la carpeta Django.
