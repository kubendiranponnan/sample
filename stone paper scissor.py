import random
a=["stone","paper","scissor"]
b=["stone","paper","scissor"]
c=random.choice(a)
d=random.choice(b)
b[0]>a[1]
b[1]>a[2]
b[2]>a[0]
a[0]>b[1]
a[1]>b[2]
a[2]>b[0]
a[0]=b[0]
a[1]=b[1]
a[2]=b[2]
if(c==d):
    print("tie")
if(c>d):
    print("player a wins")
if(c<d):
    print("player b wins")
