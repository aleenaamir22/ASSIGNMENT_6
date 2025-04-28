#16.Function Decorators
#Assignment:
#Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

def log_function_call(func):#func
    def call():
        print("Function is being called.")
        func()#calling func
    return call
@log_function_call#applying decorator
def say_hello():
    print("Welcome back!")    

#creating object
say_hello()

#output:
#Function is being called.
#Welcome back!