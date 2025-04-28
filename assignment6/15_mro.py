#15. Method Resolution Order (MRO) and Diamond Inheritance
#Assignment:
#Create four classes:
#A with a method show(),
#B and C that inherit from A and override show(),
#D that inherits from both B and C.
#Create an object of D and call show() to observe MRO.

#Four classes
class A:
    def show(self):#method
        print("A for apple")
class B(A):
    def show(self):
        print("B for ball")
class C(A):
    def show(self):
        print("C for cat")
class D(B,C):    
     pass

#creating object

d1=D()
d1.show()

#output
#B for ball



# What's happening step-by-step?
#You created a class D(B, C).
#D inherits from B first, then C.
#When you call d1.show(), Python looks for the show() method.
#Python searches following the MRO order:
#First in D itself → no show() method.
#Then in B (first parent) → B has show(), so it calls B's method!
#It does not check C or A after finding it in B.

#D → B → C → A → object
#D (no show() method)
#B (show() found → stop searching)
#(C and A are not checked)