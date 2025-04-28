#using cls
#Assignment
#Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:#created a class counter
    count=0#using class variable

    def __init__(self):
        Counter.count += 1
    @classmethod#using class method
    def display(cls):#class methid is making display a class method
        print(f"Total objects created:{cls.count}")
#creating object
c1 = Counter()
c2 = Counter()
#calling class method & displaying total count
Counter.display()            
           
#output:
#Total objects created:2           