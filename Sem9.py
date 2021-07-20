
import datetime
import os

CWD = os.path.dirname(__file__)

#! Ejercicios viernes

#* Formas de importar módulos (librerías externas)
#? import + nombre, para importar toda la librería.
#? import + nombre + as + como lo quieras llamar, para lo mismo que antes.
#? from + nobmre + import +  lo que quieras importar de la librería, para no importar la librería entera. Puedes importar varias cosas separándolas por comas. Si quisieras importarlo con este formato, puedes poner un asterisco y lo importa todo.

#! Ejercicios martes

#* Librería Datetime

#? Lo primero de todo es importar la librería «datetime».

#* En el caso de que queramos introducir la fecha manualmente usaremos el atributo «date» de la clase «datetime».
date = datetime.date(2021, 7, 20)
print(date)
print(date.day)

#* Para sumar días a «datetime» (con «timedelta»).

ten_days = datetime.timedelta(days = 10)
print(date + ten_days)

#* Cómo caducan las contraseñas.

today = datetime.datetime.today()
print(today)
print(today.month)

contraseña_vip = 'contraseña'
contraseña_vip_caduca = today + datetime.timedelta(days = 1)
print(contraseña_vip_caduca) #TODO Para que caduque al día siguiente despuésw de inicializarse.

if today < contraseña_vip_caduca:
    print('Continuamos')

#? Para pasar un dato de usuario de str a date y viceversa:

#! Esto es una forma artesanal

# # user_date = input('YYYY-MM-DD: ')
# dec_user_date = [int(value) for value in user_date.split('-')]
# date_1 = datetime.date(dec_user_date[0], dec_user_date[1], dec_user_date[2])

#* Con los atributos «isoformat» y «fromisoformat»:

date_str = date.isoformat()
print(date_str)

date_iso = date.fromisoformat(date_str)
print(date_iso)

#* Para crear un fichero de login «.log»:

# with open(f'{CWD}/histórico.log', 'w', encoding = 'utf8') as file:
#     file.write('Lo que queramos')

with open(f'{CWD}/histórico.log', 'a', encoding = 'utf8') as file:
    file.write(f'{datetime.datetime.today().isoformat()}| 200 | user post |\n')