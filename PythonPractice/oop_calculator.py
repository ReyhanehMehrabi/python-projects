#step 1 create the class
class Calculator:
    #methods no longer function
    #name = "My Calculator"
    #self is an access pointer to orderwise hidden class members
    #the __init__ is called a constructor
    #Automatically called by python on object creation
    def __init__(self,num1,num2):
        self.number1 = num1
        self.number2 = num2
        
    def add(self):
        result = self.number1 + self.number2
        return result

    def subtract(self):
        result = self.number1 - self.number2
        return result

    def multiply(self):
        result = self.number1 * self.number2
        return result


    def divide(self):
        result = self.number1 / self.number2
        return result


    def double_divide(self):
        result = self.number1 // self.number2
        return result


    def modulus(self):
        result = self.number1 % self.number2
        return result


# create an object using the calculator blueprint
#step 2 create object of the class
sc_calc = Calculator(5,8) # () is a constructor
sc_calc2 = Calculator(9,6)  # () is a constructor
#print(sc_calc.add(4,9))
#sc_calc.name = "Scientific Calculator"
#print(sc_calc.name)
#print(type(sc_calc))
#print(type(sc_calc2))

add_result = sc_calc.add()
add_result2 = sc_calc2.add()
print(add_result)

 