# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:29:11 2022

@author: minut
"""

def add(num1,num2):
    return num1 + num2
    #student writes code
def subtract (num1,num2):
    return num1 - num2
    #student writes code
def multiply(num1,num2):
    return num1 * num2
    #student writes code
def divide (num1,num2):
    return num1 / num2
    #student writes code
    
def calculator(num1, num2, operator):
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        return "Please choose a valid operator (+, -, *, /)"

    return result    

num1 = float(input('enter first number: '))
operator = input('enter the operator: ')
num2 = float(input('enter second number: '))


calc_output = calculator(num1, num2, operator)
print(f'Result: {num1} {operator} {num2} = {calc_output}')