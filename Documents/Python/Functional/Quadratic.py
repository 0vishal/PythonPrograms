'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To get the root of a quadratic equation
'''

import math

try:
a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
c = int(input("Enter the value of c"))
except ValueError:
    print("Enter the correct integer value")

#a function to calculate the roots of quadratic equation
def qEquation():
    try:
        delta = math.pow(b,2)-(4*a*c)
        root1 = (-b+math.sqrt(delta))/(2*a)
        root2 = (-b-math.sqrt(delta))/(2*a)
        print(root1)
        print(root2)
    except NameError as e:
        print(e) 
"""
Description:
 A function to calculate roots of the quadratic equation using delta formula 
Parameter:
a b and c are the values used in the functions for calculation of roots
"""          
qEquation()
   