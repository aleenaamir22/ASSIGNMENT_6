#roperty Decorators: @property, @setter, and @deleter
#Assignment
#Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self,price):
        self._price=price

        @property  #to get price
        def price(self):
           return self._price
        
        @price.setter #to set price
        def price(self,value):
            self._price=value

        @price.deleter   #to delete price
        def price(self):
            del self._price 
#creating object
#getting price
price1=Product(200)
print(price1._price)
#setting price
price1._price=300
print(price1._price)    
#deleting price 
del price1._price

#output
#200 
#300 