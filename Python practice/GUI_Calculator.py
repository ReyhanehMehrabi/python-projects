# Module 07 Lab11 and Lab12
import PySimpleGUI as sg

from calculator import add, subtract, multiply, modulus, divide, double_divide

# Layout   
# # Create GUI
layout = [[sg.Txt('' * 30)],
          [sg.Text('', size=(15, 1), font=('Times New Roman', 26),
                   text_color='red', key='input')],
          [sg.ReadFormButton('7'), sg.ReadFormButton(
              '8'), sg.ReadFormButton('9'), sg.ReadFormButton('÷')],
          [sg.ReadFormButton('4'), sg.ReadFormButton(
              '5'), sg.ReadFormButton('6'), sg.ReadFormButton('x')],
          [sg.ReadFormButton('1'), sg.ReadFormButton(
              '2'), sg.ReadFormButton('3'), sg.ReadFormButton('-')],
          [sg.ReadFormButton('0'), sg.ReadFormButton(
              '//'), sg.ReadFormButton('+'), sg.ReadFormButton('%')],
          [sg.ReadFormButton('c'), sg.ReadFormButton(
              '='), sg.ReadFormButton('x^2'), sg.ReadFormButton("sqrt")]
          ]


# Set PySimpleGUI
form = sg.FlexForm('Module07_Lab', default_button_element_size=(
    5, 2), auto_size_buttons=False, grab_anywhere=False)
form.Layout(layout)

# Set Process
Equal = '' # 5+6, 7-3,


# Loop
while True:
    button, value = form.Read()                            # call GUI

    # Press Button
    if button is 'c':
        Equal = ''
        form.FindElement('input').Update(Equal)
    elif button is '+':
        Equal += '+'
        print(Equal)
        form.FindElement('input').Update(Equal)
    elif button is '-':
        Equal += '-'
        form.FindElement('input').Update(Equal)
    elif button is 'x':
        Equal += '*'
        form.FindElement('input').Update(Equal)
    elif button is '÷':
        Equal += '/'
        form.FindElement('input').Update(Equal)
    elif button is '%':
        Equal += '%'
        form.FindElement('input').Update(Equal)
    elif button is '//':
        Equal += '//'
        form.FindElement('input').Update(Equal)
    elif button is 'x^2':
        Equal += '**'
        form.FindElement('input').Update(Equal)
    elif button is 'sqrt':
        form.FindElement('input').Update(Equal)
    elif str(button) in '0123456789':
        Equal += str(button)
        form.FindElement('input').Update(Equal)
    elif button is '=':
        #Data for calculator
        # "4/2"
        operator2 = ""
        if len(Equal) == 3:
            num1 = int(Equal[0])
            operator = Equal[1]
            num2 = int(Equal[2])
        else:
            # "4//2"
            num1 = int(Equal[0])
            operator = Equal[1]
            operator2 = Equal[2]
            num2 = int(Equal[3])
        if operator == "+":
            result_of_calc = add(num1,num2)
            form.FindElement('input').Update(result_of_calc)# display on the screen
        elif operator == "-":
            result_of_calc = subtract(num1, num2)
            form.FindElement('input').Update(result_of_calc) # display on the screen
        elif operator == "/" and operator2 == "/":
            result_of_calc = double_divide(num1, num2)
            form.FindElement('input').Update(
                result_of_calc)  # display on the screen
        elif operator == "/":
            result_of_calc = divide(num1, num2)
            form.FindElement('input').Update(result_of_calc) # display on the screen
        
        elif operator == "*":
            result_of_calc = multiply(num1, num2)
            form.FindElement('input').Update(result_of_calc)
        elif operator == "%":
            result_of_calc = modulus(num1, num2)
            form.FindElement('input').Update(result_of_calc)
    elif button is 'Quit' or button is None:                            # QUIT Program
        break
