'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : Get the values which have sum of 3 integers zero in array
'''

try:
    number = int(input("Enter the number of integers "))
except:
    print("Enter a positive integer value")

#To create a array and input values
arr = []
for i in range(number):
    try:
    value = int(input("Enter the value  "))
    except ValueError:
        print("Enter correct integer value")
    arr.append(value)

#To check the sum of array values in triples is zero 
def sumOfIntegers():
    try: 
        count=0
        for i in range(number-2):
            for j in range(i+1,number-1):
                for k in range(j+1, number):
                    if(arr[i] + arr[j] + arr[k] == 0):
                        print(arr[i], arr[j], arr[k])
                        count+=1
    except NameError as e:
        print(e) 
"""
Description:
 A function for values calculation of sum of triplets value equal zero
Parameter:
an array values are used to compare and calculate  
"""                     
sumOfIntegers()

print("The number of triples equal to zero are " count)                