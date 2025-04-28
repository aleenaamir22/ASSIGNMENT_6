#using self
#Assignment:
#Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.


class students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"{self.name} secures {self.marks} marks.")
#creating object,calling display
s=students("Alice",97)
s.display()

#Output
#Alice secures 97 marks.