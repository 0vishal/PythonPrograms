'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To take input in 2D array and print it
'''
try:
    rows = int(input("Enter the number of rows "))
    columns = int(input("Enter the number of columns "))
except ValueError: 
    print("Enter correct input")

#To create function of 2D array, Input values and print it.
    def createArray():
        try:
            arr=[]
            for i in range(rows):
                value = []
                for j in range(columns):
                    val = int(input("Enter the value  "))
                    value.append(val)
                arr.append(value)
                print(arr)
        except NameError as e:
            print(e)

"""
Description:
 A function to create an array and take input value for array and print it 
Parameter:
rows and columns are parameters used for dimensions of array
"""            
createArray()                
