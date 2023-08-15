#!/usr/bin/env python3

def greet_programmer():
    print('Hello, programmer!')

greet_programmer()
    

def greet(name):
    print('Hello, ' + name + "!")
greet("Isaack")

def greet_with_default(name="programmer"):
    print("Hello, " + name + "!")
greet_with_default("William")

def add(num1, num2):
    return num1 + num2
result = add(5,3)
print(result)

def halve(number):
    return number/2
result = halve(10)
print(result)
