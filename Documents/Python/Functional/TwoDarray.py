#To create function of 2D array, Input values and print it.
rows = int(input("Enter the number of rows "))
columns = int(input("Enter the number of columns "))

def createArray():
    arr=[]
    for i in range(rows):
        value = []
        for j in range(columns):
            val = int(input("Enter the value  "))
            value.append(val)
        arr.append(value)
        print(arr)

createArray()                