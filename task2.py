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
#Way 1

#for i in range(1,4):
#    x=str(input(f"This is guess {i}.\nEnter your username.=>"))
#    if x==expectedUsername:
#        print('Correct')
#        for m in range(1,4):
#            y=str(input(f"\nThis is guess {m}.\nEnter your password.=>"))
#            if y==expectedPassword:
#                print('Access Granted')
#                exit()
#        else:
#            print('Access Denied')
#            break
#else:
#    print('Access Denied')

#Way 2

for q in range(1,4):
    unm=input(f"This is guess {q}.\nEnter your username.=>")
    pwd=input(f"This is guess {q}.\nEnter your password.=>")
    if unm==expectedUsername and pwd==expectedPassword:
        print('Access Granted.')
        break
    else:
        print('Incorrect')
else:
    print('Access Denied.')