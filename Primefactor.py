#To get the prime factor of the numbergit git git 
number = int(input("Enter the value of N"))

for x in range(2,number):
    while(number%x==0):
        print(x)
        number=number/x
        