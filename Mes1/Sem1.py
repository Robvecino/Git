import random #! Las bibliotecas se importan al principio
# nombre = 'Roberto'
# apellido = 'Vecino'
# apellido = 'Vecino Alonso'
# edad = 31
# print('Rober')
# print(nombre)
# x = 4
# y = 2
# print(x + y)
# print(1 == 1)

# #* IF STATEMENTS

# if edad >= 18:
#     print('Es adulto')
# else:
#     print('No es adulto')

# #Métodos

# print(apellido.upper())
# nombre_completo = 'Roberto Vecino Alonso'
# result = nombre_completo.replace('Roberto', 'Rober')
# print(result)

#!Ejercicio lunes

# lorem = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of 'de Finibus Bonorum et Malorum' (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, 'Lorem ipsum dolor sit amet..'"

#*Ejercicio 1
# a = "hola"
# b = "Hola"
# print(a == b.lower())

# #*Ejercicio 3
# print(lorem.count('it') + lorem.count('It'))

# *#Ejercicio 4
# print(lorem.count('Ipsum'))
# print(lorem.find('Ipsum'))
# print(lorem[34:39])

#*Ejercicio 5
# print(lorem.count(' ') + 1)

# #*Ejercicio 6
# ri = lorem.find('Richard')
# resultado = lorem[ri : 171]
# #Ejercicio 7
# print(resultado.lower())

# #*Ejercicio 8
# lista_palabras = lorem.split(' ')
# print(lista_palabras)

# #*Ejercicio 9

# password = "contraseña"
# password.encode() #No va así.

# #*Ejercicio 10
# password.capitalize()
# password.replace('o','u')
# password.replace('a', 'e')
# password.replace('e', 'i')
# password + str(len(password))

#!Ejercicio martes

#*Ejercicio 12, 13 y 14

# if len(lista_palabras) >= 100:
#     print(lorem.upper())
# elif len(lista_palabras) >= 80:
#     print(lorem.replace('Richard', 'Ricardo'))
# else:
#     print(lorem.replace('Virginia', 'Salamanca'))

# #*Otra forma:
# if len(lista_palabras) >= 100:
#     print(lorem.upper())
#     if len(lista_palabras) >= 80:
#         print(lorem.replace('Richard', 'Ricardo'))
#     elif len(lista_palabras) < 80 and len(lista_palabras) > 0:
#         print(lorem.replace('Virginia', 'Salamanca'))
# #*Ejercicio 15

# palabra = input('Introduzca una palabra: ')
# if lorem.find(palabra) >= 0:
#     print('Esta palabra forma parte del texto')
# else:
#     print('Esta palabra no se encuentra en el texto')

#*Otra forma

# palabra = input('Introduzca una palabra: ')
# palabra_indice = lorem.find(palabra)
# if lorem.find(palabra) >= 0:
#     print(f'Se ha encontrado su palabra en este contexto: {lorem[palabra_indice:palabra_indice + 21]}...')
# else:
#     print('No se ha encontrado su palabra en el texto')


#Para dar formato #!el método anterior de '.format' ya no se utiliza
# print(f'Imprímeme bien el {lorem}')

#!Ejercicios miércoles
#*Ejercicio 16

# user = input('Make your choice: ')
# picks = ['rock','paper','scissors']
# pc = (random.choice(picks))
# print(pc)

# if user == pc:
#     print('Tie')
# elif user == picks[0] and pc == picks[2]:
#     print ('You win')
# elif user == picks[2] and pc == picks[0]:
#     print('You lose')
# elif picks.index(user) > picks.index(pc):
#     print('You win')
# else:
#     print('You lose')

# #*Otra forma
# user = input('Make your choice: ')
# picks = ['rock','paper','scissors']
# pc = (random.choice(picks))
# print(pc)

# if user == pc:
#     print('Tie')
# else:
#     if user == 'rock':
#         if pc == 'paper':
#             print('You lose')
#         else:
#             print('You win')
#     elif user == 'paper':
#         if pc == 'scissors':
#             print('You lose')
#         else:
#             print('You win')
#     else:
#         if pc == 'rock':
#             print('You lose')
#         else:
#             print('You win')

## *#Otra forma
# user = input('Make your choice: ')
# picks = ['rock','paper','scissors']
# pc = (random.choice(picks))
# print(pc)

# if user == pc:
#     print('Tie')
# else:
#     if user == 'rock' and  pc == 'paper':
#             print('You lose')
#     elif user == 'paper' and pc == 'scissors':
#             print('You lose')
#     elif user == 'scissors' and pc == 'rock':
#             print('You lose')
#     else:
#         print('You win')

#!Ejercicios jueves

# test = [1,2,3,4]
# test.pop(0)
# test.pop(0 + 2)
# print(test)
# test.index(3)

#*Otra forma con pop

# user = input('Make your choice: ')
# picks = ['rock','paper','scissors']
# pc = (random.choice(picks))
# print(pc)

# if user == pc:
#     print('Tie')
# else:
#     picks.pop(picks.index(user))
#     if user == 'paper':
#         if pc == picks[1]:
#             print('You lose')
#         else:
#             print('You win')
#     else:
#         if pc == picks[0]:
#             print('You lose')
#         else:
#             print('You win')

# test = [2,4,5,76]
# test.sort() #Este método modifica la lista; es destructible.
# sorted(test) #Esta función no modifica la lista; no es destructible. Crea una nueva lista ordenada, por lo que se puede meter dentro de una variable.
# print(test)

#!Bucles
#?While

# test = [1,2,3,4]
# count = 0
# while count < 4:
#     print(count)
#     count += 1

# test_2 = ['a','b','c','d','e']
# count = 0
# while count < len(test_2):
#     user = input('Búsca: ')
#     print(test_2.index(user))
#     count += 1

# user = input('Inserte una letra: ')
# while True:
#     if user in test_2:
#         print(test_2.index(user))
#     else:
#         break
# print('Esta letra no se encuentra en la lista')






