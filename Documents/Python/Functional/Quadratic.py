#a function to calculate the roots of quadratic equation
import math
a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
c = int(input("Enter the value of c"))

def qEquation():
    delta = math.pow(b,2)-(4*a*c)
    root1 = (-b+math.sqrt(delta))/(2*a)
    root2 = (-b-math.sqrt(delta))/(2*a)
    print(root1)
    print(root2)

qEquation()