#20. Creating a Custom Exception
#Assignment:
#Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("You're underage.Age must be atleat 18 to ride a bike.")
    print("Age is valid")

#creating object
try:
    check_age(14)
except InvalidAgeError as i:
    print(i)  

#output: You're underage.Age must be atleat 18 to ride a bike.     

try:
    check_age(27)
except InvalidAgeError as i:
    print(i)    

#output: Age is valid  