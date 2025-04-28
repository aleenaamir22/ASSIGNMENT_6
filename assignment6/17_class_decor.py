#Class decorator
#Assignment:
#Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

def add_greeting(cls):
    def greet(self):
        return "Hello from decorator!"
    cls.greet=greet
    return cls

@add_greeting
class Person:
    def __init__(self,name):
        self.name=name

#creating object    
p1=Person("Alice")   
print(p1.greet())

#output:
#Hello from decorator!