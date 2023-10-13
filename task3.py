#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwordlist = ["12345","password","iloveyou","mom","default","0"]
username=str(input('Enter your username=>'))
password=str(input('Enter your password=>'))
for i in range(6):
    #print(i,users[i],passwordlist[i])
    if username==users[i] and password==passwordlist[i]:
        print('Access granted')
        break
else:
    print('Access denied')