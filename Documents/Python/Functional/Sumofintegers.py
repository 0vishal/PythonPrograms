
number = int(input("Enter the number of integers "))
#To create a array and input values
arr = []
for i in range(number):
    value = int(input("Enter the value  "))
    arr.append(value)

#To check the sum of array values in triples is zero 
def sumOfIntegers():
    count=0
    for i in range(number-2):
        for j in range(i+1,number-1):
            for k in range(j+1, number):
                if(arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    count+=1
sumOfIntegers()                    
print("The number of triples equal to zero are " count)                