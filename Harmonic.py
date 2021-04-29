'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To get the Nth Harmonic number
'''

#To get the Nth Harmonic number
from fractions import Fraction

try:
    number = int(input("Enter the power of N"))
except ValueError:
    print("Enter the positive value")
x=1
series=1
try:
    for x in range(1,number+1):
        series=Fraction(1/x)
    print(series)
except NameError as e:
    print(e) 