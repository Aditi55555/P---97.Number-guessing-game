import random
num = random.random() * 1-9
chances=1

while chances <=3:
    enterrandom = input("enter a number between 1 and 9:")
    if enterrandom == num :
        print ("Congratulations! you're right")
        break
    else:
        print("try again")
    chances=chances+1
if chances==3:
    print("You lose. the number is:",num)









