'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To calculate to win percentage of a game 
'''
import random

#To take input of Stake Goal and number of times 
try:
    stake = int(input("Enter the stake amount to start with: "))
    goal = int(input("Enter the goal amount to reach: "))
    time = int(input("Enter the number of times to run "))

except ValueError:
    print("Enter the correct input")

  
#a function to run N number of times and bet stake until goal is reached or becomes zero.
def game():
    count=0
    win=0  
    for i in range(time):
        bet = stake  
        while bet > 0 and bet < goal:
            count += 1 
            if random.randint(0,1) == 0:
                bet += 1
            else:
                bet -= 1
               
        if bet == goal:
            win += 1
    print(win/time*100)
    print(bet) 
"""
Description:
A game function is created to calculate N number of times and bet stake until goal is reached or becomes zero.
Parameter:
bet parameter is used for betting on every time. Goal parameter is the goal of game. Win parameter is used to calculate the win percentage of the game.
"""
try:
    game()
except NameError as e:
    print(e)