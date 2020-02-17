for i in range(0,3):
    for j in range(0,5):
        if(i==2 or i==j==1 or (i==0 and j==2) or (i==1 and j==3) or (i==1 and j==2)):
            print("+",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
