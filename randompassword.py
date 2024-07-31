from random import *
from string import *
print("welcome to the random password generator:")
char = ascii_letters
char+= digits
char+= punctuation
while True:
    y=int(input('''
    1. Generate a new password
    2. exit\n'''))
    if y==1:
        len=int(input("Enter Length: "))
        password=""
        for i in range(len):
            password+= choice(char)
        print("Your Random Password is: ",password)
    elif y==2:
        break
    else:
        print("invalid choice")
