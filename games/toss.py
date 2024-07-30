from random import *
l=["Head", "Tail"]
while True:
    i=int(input('''
1. Toss
2. Exit\n'''))
    if i==1:
        print(choice(l))
    else:
        break;