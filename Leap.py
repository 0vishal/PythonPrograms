@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To check a year is leap year or not 

#To check a year is leap year or not
try:
    year = int(input("Enter a year: "))
except ValueError:
    print("Enter a correct year")    

try:
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(year, "is a leap year")
            else:
                print(year, "is not  a leap year")
        else:
            print(year, "is a leap year")
    else:
        print(year, "is not  a leap year")
except NameError as e:
    print(e)        