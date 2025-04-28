#12.static method
#assignment
#Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:  #class

    @staticmethod       #static method
    def celcius_to_fahrenheit(c):#method
        return  (c*9/5 )+ 32 #formula #returning fahreheit value
    
#creating object
print(f"{TemperatureConverter.celcius_to_fahrenheit(5)}°F")

# output    
#41.0°F