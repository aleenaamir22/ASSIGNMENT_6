#8.the super() function
#Assignment:
#Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:#class
    def __init__(self,name):#constructor
        self.name=name
class Teacher(Person):#inherit a class teacher
    def __init__(self,name,subject):
        super().__init__(name)      #using super()
        self.subject=subject  

#creating object
t1=Teacher("Maria","Science")
print(t1.name)
print(t1.subject)
print(t1.name,t1.subject)

#output:
#Maria , Science ,Maria Science