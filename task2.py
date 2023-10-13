#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''

expectedUsername = "systemadmin"
expectedPassword = "master"
y=expectedPassword

for i in range(1,4):
    x=str(input(f"This is guess {i}.\nEnter your username.=>"))
    if x==expectedUsername:
        print('Correct')
        for m in range(1,4):
            y=str(input(f"\nThis is guess {m}.\nEnter your password.=>"))
            if y==expectedPassword:
                print('Access Granted')
                exit()
        else:
            break
        
else:
    print('Access Denied')