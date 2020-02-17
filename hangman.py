a=""
print("HANGMANN \n""GAME ON")
j==2
for i in range(0,3):
    print("Question:  ")
    print("Answer:  ---------  ")
    b=input()
    j==j-1
    if(a==b):
        print("***YOU WON***")
        break
    else:
        print("---YOU LOST---")
        print("You have more" )
