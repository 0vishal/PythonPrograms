@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To Print USername with String 

#To get the username with string
try:
    username = input("Enter the value: ")
except ValueError:
    print("Enter correct username in string")

if len(username) < 3:
    print("Username should have minimum 3 characters")
else:
    print("Hello", username, "How are You ?") 
