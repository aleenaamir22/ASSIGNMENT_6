#21. Make a Custom Class Iterable
#assignment 
#Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self,start):
        self.start=start

    def __iter__(self):
        return self

    def __next__(self):    
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -=1
        return current


#creating object
for number in Countdown(10):
    print(number)
#output
#10 
# 9 
# 8 
# 7 
# 6 
# 5 
# 4 
# 3 
# 2 
# 1 
# 0  
