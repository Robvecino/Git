
#! Ejercicios martes

#* POO

municipio_1 = {'mun_id' : '222245', 'den_km2' : 4.44, 'area' : 143215}

municipio_2 = {'mun_id' : '222666', 'den_km2' : 4.94, 'area' : 164315}

#TODO Un objeto es como un diccionario, en el que podemos añadir funciones para que realicen acciones dentro del objeto (funcionalidades).

#! Ejercicios miércoles

#? Se comienza con la palabra «class». Los objetos, por convencion, se deben capitalizar. Las clases básicas no llevan paréntesis después del nombre. Después van dos puntos y le sigue «def __init__(self):».
#* La función «__init__» se ejecutará una sola vez
class Mun:
    def __init__(self, mun_id, den_km2, area):
        self.mun_id = mun_id
        self.den_km2 = den_km2
        self.area = area
    def population(self):
        return self.den_km2 * self.area

#? Las líneas de código con «.self» son los atributos de la clase. Dentro de las clases, podemos introducir métodos específicos para definir instancias. En nuestro ejemplo, «population». Dichas instancias tienen que tener, como mínimo la variable «self»
obj_mun_1 = Mun('222245', 4.44, 143215) #TODO Esto sería una instancia de la clase «Mun».
obj_mun_2 = Mun('228945', 4.09, 143475)
print(obj_mun_1.den_km2)
print(obj_mun_1.population())
print(obj_mun_2.population())

class Human:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
    def imc(self):
        return (self.weight / self.height ** 2)

andres = Human('Andrés', 70, 1.76)
renzo = Human('Renzo', 76.4, 1.87)

print(f'IMC de Andrés: {andres.imc()}')
print(f'IMC de Renzo: {renzo.imc()}')

# for human in list_humans:
#     result = 0
#     a = Human(human['name'], human['weight'], human['height'])
#     result += a.imc()
#     print(sum(result)/len(result))

#! Ver «pokemon.py» para más ejemplos.