'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To take temperature and Speed input to calculate the windChill 
'''
import math

try:
    t = int(input("Enter the temperature Fahrenheit"))
    v = int(input("Enter the speed miles per hour"))
except:
    print("Enter the correct value of temperature in fahrenheit and speed in miles per hour")

#To calculate the windChill 
def windChill():
    try:
        w = (35.74 + 0.6215*t + (0.4275*t - 35.75)*math.pow(v,0.16))
        print(w)
    except NameError as e:
        print(e)
"""
Description:
 A function to calculate the wind chill using the formula and print it
Parameter:
t and v are parameters used in function as temperature and speed for wind chill calculation
"""          
windChill()    

