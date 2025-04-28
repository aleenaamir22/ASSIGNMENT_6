#public variable and methods
#Assignment:
#Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        #public variable
        self.brand = brand
#public method
    def start(self):
       print(f"{self.brand} car is starting")    

#creating object
car1=Car("Toyota")       
car1.start()#calling public method
print(car1.brand)#printing the brand of the car