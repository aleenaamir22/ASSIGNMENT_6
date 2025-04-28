#13.Composition
# #Assignment:
#Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:#class
    def start(self):#method
        print("Engine started......")
class Car:#class
    def __init__(self,engine):
       self.engine=engine
    def start(self):#method
        self.engine.start()   

#creating object
e1=Engine()
c1=Car(e1)
c1.start()

#output
#Engine started....