from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car started")
c = Car()
c.start()

from abc import ABC, abstractmethod
    
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self, radius):
       print("Area of Circle: = 7.85")

c = Circle()
c.area(5)