#To get the power of N
number = int(input("Enter the power of N"))

power = 1
N = 2
if 0 < number < 31:
    for x in range(0,number):
        power = (power*N)
        print(power)
else:
    print("Power of 2 overflows")        

    
