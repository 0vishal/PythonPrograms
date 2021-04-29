'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To calculate the Euclidean distance of a number
'''

import math

try:
x = int(input("Enter the value of x "))
y = int(input("Enter the value of y "))
except ValueError: 
    print("Enter positive integer of x and y")
a,b = (0,0)

#Create a function to calculate Euclidean distance
def eDistance():
    try:
        edistance = math.sqrt(math.pow(x-a,2)+math.pow(y-b,2))
        print(edistance)
    except NameError as e:
        print(e)
"""
Description:
 A function to calculate the euclidean distance
Parameter:
x and y are the points to calculate the euclidean distance
"""                    
eDistance()
