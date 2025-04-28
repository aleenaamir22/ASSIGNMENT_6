#Assignment:Access Modifiers: Public, Private, and Protected
#Create a class Employee with:
#a public variable name, #a protected variable _salary, and #a private variable __ssn.
#Try accessing all three variables from an object of the class and document what happens.

class Employe:
    def __init__(self,name,salary,ssn):
        self.name=name           #public variable .
        self._salary=salary      #protected variable ._
        self.__ssn=ssn           #private variable .__   #ssn stands for social security number

    def private(self):
        return self.__ssn    

#creating object
e1=Employe("mehtab",30000,"234-56-9899") #employe details

#printing details
print(e1.name) #name will be print
print(e1._salary) #salary will be printed
#print(e1.__ssn) #attribute error
print(e1.private())
        
#output:
# mehtab 
# 30000
# 234-56-9899        