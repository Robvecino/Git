
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
        self.mun_id = mun_id #? Esto es un atributo de la clase «mun»
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

#! Ejercicios viernes:

#* Dentro de nuestra clase «Pokemon», podemos iniciar un contador para tener una cantidad específica de pokemons creados. Cada instancia de la clase, aumenta en 1 el contador. Dicho contador debe estar dentro de la clase, pero fuera de la función «init». Este contador actuaría de propiedad de clase.

class Animal:
    count = 0

    def set_count(value):
        Animal.count += value #? En este caso, se introduce Animal para hacer referencia a la clase; en el caso de que quisiésemos que afectase a una instancia, deberíamos usar «self».
    # @classmethod #TODO Se puede usar este decorador (este código que comienza por arroba) para poder usar «cls» y no tener que citar la clase.
    # def set_count(cls, value):
    #     cls.count += value 

    def __init__(self, name):
        self.name = name
        Animal.set_count(1)

    def __str__(self):
        return f'{self.name}'

perro = Animal('Kuga')
gato = Animal('José')
print(perro)
print(Animal.count)

#! Ejercicios lunes:

class Employee:
    subida = 1.02 #* Este atributo se pone por encima de «init» porque debe afectar a todos los empleados. Igual que en el caso del contador de la clase de animal.

#* Ejemplo de decoradores:

class Mun:
    annual_growth = 1.03
    def __init__(self, ine, density, area):
        self.ine = ine
        self.density = density
        self.area = area
    @property
    def population(self):
        return self.area * self.density
    def apply_annual_growth(self, value):
        return self.population * value

mun_1 = Mun('28009', 3, 15)
print(mun_1.population) #? Al usar el decorador «property», no hace falta llamrlo como método, sino como atributo.
print(mun_1.population)