
import datetime
#! Ejercicios jueves

#* En POO hay métodos y propiedades de clase, así como lo mismo para las instancias. Hay que pensar si el método o la propiedad afecta al método o a la instancia. Existen otros métodos llamdos «métodos estáticos» que no trabajan con las propiedasdes de la clase de manera estrecha. Uno de los pilares de los objetos es la encapsulación. Estos métodos no trabajan con los métodos de las clases ni con los de las instancias.

class Employee:

    salary_raise = 1.02 #? Propiedad de clase

    def __init__(self, name, surname, salary):
        self.name = name #? Propiedad de instancia
        self.surname = surname
        self.salary = salary
        self.workdays = []

    def __str__(self):
        return f'{self.name} - {self.surname}' #? Método de instancia
    
    @classmethod
    def set_salary_raise(cls, value):
        cls.salary_raise = value #? Método de clase

    @staticmethod
    def is_sunday(): #? Método estático
        day = datetime.date.today()
        return True if day.isoweekday() == 7 else False
    
    # def get_salary():
    #     sunday = 0
    #     for day in workdays:
    #         is_sunday() == True:
    #             sunday += 1
    #     return (len(workdays) - sundays)) + (sundays * (workdays - sundays) * 1.5)
    

test = Employee('Vito', 'Genovese', 10.30)
print(test.is_sunday())
