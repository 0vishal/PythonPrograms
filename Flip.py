import random
#To get the head tail percentage the number of times a coin is flipped
head=0
tail=0

number = int(input("Number of times to flip a coin"))

if number < 0:
    print("Enter a positive integer")
else:
    for x in range(0,number):
        flip = random.random()
        if flip < 0.5:
            head+=1
        else:
            tail+=1

headpercent = (head/number)*100
tailpercent = (tail/number)*100
print("head percentage",headpercent,"tail percentage",tailpercent) 

