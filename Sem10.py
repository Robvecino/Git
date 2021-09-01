
import datetime
# #! Ejercicios jueves

# #* En POO hay métodos y propiedades de clase, así como lo mismo para las instancias. Hay que pensar si el método o la propiedad afecta al método o a la instancia. Existen otros métodos llamdos «métodos estáticos» que no trabajan con las propiedasdes de la clase de manera estrecha. Uno de los pilares de los objetos es la encapsulación. Estos métodos no trabajan con los métodos de las clases ni con los de las instancias.

# class Employee:

#     salary_raise = 1.02 #? Propiedad de clase

#     def __init__(self, name, surname, salary):
#         self.name = name #? Propiedad de instancia
#         self.surname = surname
#         self.salary = salary
#         self.workdays = []

#     def __str__(self):
#         return f'{self.name} - {self.surname}' #? Método de instancia
    
#     @classmethod
#     def set_salary_raise(cls, value):
#         cls.salary_raise = value #? Método de clase

#     @staticmethod
#     def is_sunday(): #? Método estático
#         day = datetime.date.today()
#         return True if day.isoweekday() == 7 else False
    
#     # def get_salary():
#     #     sunday = 0
#     #     for day in workdays:
#     #         is_sunday() == True:
#     #             sunday += 1
#     #     return (len(workdays) - sundays)) + (sundays * (workdays - sundays) * 1.5)
    

# test = Employee('Vito', 'Genovese', 10.30)
# print(test.is_sunday())

#! Ejercicios viernas

#* Herencia de clases

class Employee:

    salary_raise = 1.04

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def __str__(self):
        return f'Name: {self.name}\nSurname: {self.surname}'

    def apply_salary_raise(self):
        self.salary *= self.salary_raise

    @classmethod
    def set_salary_raise(cls, value):
        cls.salary_raise = value

class Developer(Employee): #? Esta es la clase hija que hereda las propiedades y métodos de la clase padre.

    salary_raise = 1.1

    def __init__(self, name, surname, salary, p_language):
        super().__init__(name, surname, salary) #TODO Con la función «super», hacemos que la clase hija herede las propiedades de la clase padre. Los métodos se heredan automáticamente.
        self.p_language = p_language

    def __str__(self):
        return f'Name: {self.name}\nSurname: {self.surname}\nLanguage: {self.p_language}'

user_test = Employee('Kevin', 'James', 2000)
user_developer = Developer('Rob', 'Vecino', 2500, 'Python')

print(user_test.salary)
user_test.apply_salary_raise()
print(user_test.salary)

print(user_developer.salary)
user_developer.apply_salary_raise()
print(user_developer.salary)

Employee.salary_raise = 1.02
user_test.salary_raise()
print(user_test.salary)

#! Clase miércoles 01/09

#* Pruebas de código

#? Primero, se crean pruebas unitarias para ver si funciona el código para, después, implementar el código que se ha probado en el test. Para ello, se utiliza la librería «unittest». La explicación continúa en la carpeta «testing».

