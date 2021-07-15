
#! Ejercicio 6

class Statistics:
    def __init__(self, x, y):
        self.x = x if type(x) == list else []
        self.y = y if type(y) == list else []

#! Ejercicio 8

    @property
    def n(self):
        return len(self.x)
    

#! Ejercicio 9

    @property
    def x_mean(self):
        return sum(self.x)/self.n
    @property
    def y_mean(self):
        return sum(self.y)/self.n

#! Ejercicio 10

    @property
    def var_x(self):
        result = 0
        for num in self.x:
            result += ((num - self.x_mean) ** 2)
        var_x = result/self.n
        return var_x

#! Ejercicio 11

    @property
    def var_y(self):
        result = 0
        for num in self.y:
            result += ((num - self.y_mean) ** 2)
        var_y = result / self.n
        return var_y

#! Ejercicio 12

    @property
    def cov_x_y(self):
        result = 0
        for tupla in zip(self.x, self.y):
            result += tupla[0] * tupla[1]
        cov_x_y = (result / self.n) - self.x_mean * self.y_mean
        return cov_x_y

#! Ejercicio 13

    @property
    def rxy(self):
        return self.cov_x_y / ((self.var_x ** 0.5) * (self.var_y ** 0.5))

#! Ejercicio 14

    @property
    def B(self):
        return self.rxy / ((self.var_y ** 0.5) / (self.var_x ** 0.5))

#! Ejercicio 15

    @property
    def B0(self):
        return self.y_mean - (self.B * self.x_mean)

#! Ejercicio 16

    def prediction(self, value):
        return (self.B * value) + self.B0

test = Statistics([1, 2, 3], [4, 5, 6])
print(test.prediction(4))