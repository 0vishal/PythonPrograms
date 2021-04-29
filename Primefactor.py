@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To get the prime factor of a number

#To get the prime factor of the number
try:
    number = int(input("Enter the value of N"))
except ValueError:
    print("Enter correct value")

try:    
    for x in range(2,number):
        while(number%x==0):
            print(x)
            number=number/x
except NameError as e:
    print(e)        