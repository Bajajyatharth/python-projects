from random import *
l=["rock","paper",'scissor']
print("Rock Paper Scissor game start:")
while True:
    ys=0
    cs=0
    i=int(input('''
            1. play|start
            2. exit|stop            
            '''))
    if i==1:
        print("there are total 5 rounds:\n")
        for a in range(1,6):
            print("round"+str(a)+':')
            cc=choice(l)
            ui=int(input('''
                    please enter your choice
                         1. Rock
                         2. Paper
                         3. scissor'''))
            if ui==1:
                yc="rock"
            elif ui==2:
                yc="paper"
            else:
                yc="scissor"

            if cc==yc:
                print("computer choice",cc)
                print("your choice",yc)
                print("game draw")

            elif (yc=="rock" and cc=="scissor") or (yc=="paper" and cc=="rock") or (yc=="scissor" and cc=="paper"):
                print("computer choice",cc)
                print("your choice",yc)
                print("you wins")
                ys=ys+1
            else:
                print("computer choice",cc)
                print("your choice",yc)
                print("computer wins")
                cs=cs+1
        print("your score: ",ys)
        print("computer score: ",cs)
        if cs>ys:
            print("computer wins the game")
        elif ys>cs:
            print("you wins the game")
        else:
            print("game draw")
    elif i==2:
        break;
    else:
        print("invalid choice")
