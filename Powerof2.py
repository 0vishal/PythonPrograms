@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To get the power of N  

#To get the power of N
try: 
    number = int(input("Enter the power of N"))
except ValueError:
    print("Enter a correct positive number")    

power = 1
N = 2
try:
    if 0 < number < 31:
        for x in range(0,number):
            power = (power*N)
            print(power)
    else:
        print("Power of 2 overflows") 
except NameError as e:
    print(e)               

    
