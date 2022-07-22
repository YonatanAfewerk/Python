"""  
Assignment:
    Write a program that does the following in order:
        1. Asks the user to enter a number “x”
        2. Asks the user to enter a number “y” 
        3. Prints out number “x”, raised to the power “y”.
        4. Prints out the log (base 2) of “x”.
        
            Enter number x: 2
            Enter number y: 3
            X**y = 8
            log(x) = 1
"""
import math

x = input("Enter number x: ")
y = input("Enter number y: ")

a = int(x)
b = int(y)

c = a ** b

d = math.log(a, 2)

print("x**y = ", c)
print("Log(",x,", 2) = ", d)