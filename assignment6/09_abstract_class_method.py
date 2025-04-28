#9.Abstract classes and method
#Assignment
#Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC , abstractmethod

class Shape(ABC):#class
    @abstractmethod #abstract method
    def area(self):#method
        pass

class Rectangle():#class
    def __init__(self,width,height):
        self.width=width#variable
        self.height=height#variable

    def area(self): #method
        return self.width * self.height     

#creating object
r1=Rectangle(6,9)
print(r1.area())

#output:54