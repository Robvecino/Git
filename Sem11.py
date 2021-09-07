
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