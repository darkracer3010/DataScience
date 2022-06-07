import random
p=1
print("Welcome to the dice game")
while(p!=0):
    a=int(input("Enter your choice:"))
    ci=random.randint(1,6)
    if(a>ci):
        print("You Won")
        p-=1
    elif(a<ci):
        print("You Lost")
        p-=1
    else:
        print("It is a Tie, play again")
    
