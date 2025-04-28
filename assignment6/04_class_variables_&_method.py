#4.Class Variables and Class Methods
#Assignment:
#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:#created class
    bank_name="ABC Bank"#class variable

    @classmethod#adding class method
    def change_bank_name(cls,name):
        cls.bank_name=name

#creating object
bank1=Bank()   
Bank.change_bank_name("Jamin")  
print(bank1.bank_name)   

#output
#Jamin
    
