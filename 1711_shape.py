# 1. Создайте абстрактный класс `Shape` с абстрактным методом 
# `area()`. Реализуйте два дочерних класса — `Circle` и `Rectangle`, 
# — каждый из которых переопределяет метод `area()` для вычисления 
# площади соответствующей фигуры. Продемонстрируйте создание экземпляров 
# и вызов метода `area()` для обеих фигур.

from abc import ABC, abstractmethod
import math

class Shape(ABC):            # класс форма    
    @abstractmethod
    def area(self):         # абстрактный метод площадь
        pass

class Circle(Shape):            # подкласс  круг
    def __init__(self,radius):
        self.radius = radius

    def area(self):        
        return math.pi * (self.radius ** 2)
    
class Rectangle(Shape):     # подкласс прямоугольник
    def  __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
circle = Circle(10)    #  например радиус 5
rectangle = Rectangle(9,10)


print(circle.area())
print(rectangle.area())


