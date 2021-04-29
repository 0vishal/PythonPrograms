'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To calculate the time as stopwatch 
'''

import time

begin=0
end=0
try:
    watch = input("Enter start to Start ")
    begin=time.time()
    watch = input("Enter the stop to Stop: ")
    end=time.time()
except ValueError:
    print("Enter start/stop correctly")

totaltime = end - begin
totaltime = int(totaltime)
print(totaltime)        


