#To get the Nth Harmonic number
from fractions import Fraction

number = int(input("Enter the power of N"))

x=1
series=1
for x in range(1,number+1):
    series=Fraction(1/x)
print(series)
 