#14.Aggregation
#Assignment:
#Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Department:#class
    def __init__(self,employe):#method
        self.employe=employe#var
class Employe:  #class
    def __init__(self,name):#method
        self.name=name#var  

#creating object
e1=Employe("Ali")     
d1=Department(e1)
print(d1.employe.name) 

#output
#Ali
  