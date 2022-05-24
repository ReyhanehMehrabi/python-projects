# Function needed when imported as a module
def get_input():
    input_one = input("Please input the first number and press enter ")
    input_two = input("Please input the second number and press enter ")
    input_One = float(input_one)
    input_Two = float(input_two)
    return input_One, input_Two  # return can give back a tuple
def add(number1, number2):
    result = number1 + number2
    return result
# step 1A Lab 09 implement the body of the following functions
def subtract(number1, number2):
    result = number1 - number2
    return result
def multiply(number1, number2):
    result = number1 * number2
    return result

def divide(number1, number2):
    result = number1 / number2
    return result


def double_divide(number1, number2):
    result = number1 // number2
    return result

def modulus(number1, number2):
    result = number1 % number2
    return result
# Bonus
# step 1B create a function for BMI {body mass index}
def BMI():  # BMI = weight / height * height
    wth = input("Please give me your weigth in km and press enter key")
    hgt = input("Please give me your height in m and press enter key")
    wth_float = float(wth)
    hgt_float = float(hgt)

    bmi = wth_float / hgt_float ** 2  # height * height
    return wth_float, hgt_float, bmi

if __name__ == "__main__": # if imported __name__ == module name
    #Operation when the file is run directly
    # get user input for numbers
    input_operator = input("Please enter the operator { +, -, *, /, %, BMI}")
   
    if input_operator == "+":
        input = get_input()  # returns a tuple for input_One and input_Two
        result = add(input[0], input[1])
        print(f"Your addition of {input[0]} {input_operator} {input[1]} is: {result} ")
    # step 2 the elif and the else section
    elif input_operator == "-":
        input = get_input()  # returns a tuple for input_One and input_Two
        result = subtract(input[0], input[1])
        print(f"Your addition of {input[0]} {input_operator} {input[1]} is: {result} ")
    elif input_operator == "*":
        input = get_input()  # returns a tuple for input_One and input_Two
        result = multiply(input[0], input[1])
        print(f"Your addition of {input[0]} {input_operator} {input[1]} is: {result} ")
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
        print(f"Your weight is {input[0]} and your height is {input[1]} and your BMI is {input[2]}")
    else:
        print(f"Sorry Your operator {input_operator} is not yet supported ")
    # def add_using_input_function():
    #     input = get_input()
    #     result = input[0] + input[1]
    #     return result
