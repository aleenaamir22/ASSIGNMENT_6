#10.instance method
#Assignment
#Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:#class
    def __init__(self,name,breed):
        self.name=name#variable
        self.breed=breed#variable

    def bark(self):#instance method
        print(f"{self.name} is barking")  #printing msg

#creating object
d1=Dog("Smoky","Maltese")
d1.bark()       

#output:
#Smoky is barking
