#Create a function to calculate Euclidean distance
import math

x = int(input("Enter the value of x "))
y = int(input("Enter the value of y "))
a,b = (0,0)

def eDistance():
    edistance = math.sqrt(math.pow(x-a,2)+math.pow(y-b,2))
    print(edistance)

eDistance()