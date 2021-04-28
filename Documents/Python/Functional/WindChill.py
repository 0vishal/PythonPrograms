import math
t = int(input("Enter the temperature Fahrenheit"))
v = int(input("Enter the speed miles per hour"))

#To calculate the windChill 
def windChill():
    w = (35.74 + 0.6215*t + (0.4275*t - 35.75)*math.pow(v,0.16))
    print(w)

windChill()    