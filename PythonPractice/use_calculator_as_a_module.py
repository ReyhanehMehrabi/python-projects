
# Lab 11 make the calculator work from the module
#import calculator
from calculator import add, modulus, multiply, divide, subtract, BMI, get_input
#step 1 import the calculator module

#Operation when the file is run directly
input_operator = input("Please enter the operator { +, -, *, /, %, BMI}")
   # get user input for numbers

if input_operator == "+":
    input = get_input()  # returns a tuple for input_One and input_Two
    result = add(input[0], input[1])
    print(
            f"Your addition of {input[0]} {input_operator} {input[1]} is: {result} ")
    # step 2 the elif and the else section
elif input_operator == "-":
    input = get_input()  # returns a tuple for input_One and input_Two
    result = subtract(input[0], input[1])
    print(
            f"Your addition of {input[0]} {input_operator} {input[1]} is: {result} ")
elif input_operator == "*":
    input = get_input()  # returns a tuple for input_One and input_Two
    result = multiply(input[0], input[1])
    print(
            f"Your addition of {input[0]} {input_operator} {input[1]} is: {result} ")
elif input_operator == "/":
    input = get_input()  # returns a tuple for input_One and input_Two
    result = divide(input[0], input[1])
    print(
            f"Your addition of {input[0]} {input_operator} {input[1]} is: {result} ")
elif input_operator == "%":
    input = get_input()  # returns a tuple for input_One and input_Two
    result = modulus(input[0], input[1])
    print(
            f"Your addition of {input[0]} {input_operator} {input[1]} is: {result} ")
elif input_operator.upper() == "BMI":  # every input will be uppercase
    input = BMI()
    print(
            f"Your weight is {input[0]} and your height is {input[1]} and your BMI is {input[2]}")
else:
    print(f"Sorry Your operator {input_operator} is not yet supported ")
    # def add_using_input_function():
    #     input = get_input()
    #     result = input[0] + input[1]
    #     return result


#step 2 Think of how to make it work
# hint reuse the functions from the calculator module