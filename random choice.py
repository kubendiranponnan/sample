import random
a=int(input("enter a number  to guess "))
b=[1,2,87,5,99,34,3247,756,7,6,8]
c=random.choice(b)
if(a==c):
    print("you win")
else:
    print("you lost")
