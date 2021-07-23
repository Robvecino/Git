
import bcrypt

#* Para trabajar con contraseñas, debemos encriptarlas. Con la librería «bcrypt» podemos hacerlo.

password = input('Introduzca el password: ').encode() #TODO Como no podemos introducir la «b» de binario, le pasamos el método «encode»

password_hash = bcrypt.hashpw(password, bcrypt.gensalt()) #? De esta forma, encriptamos la contraseña.

password_decode = password_hash.decode()
