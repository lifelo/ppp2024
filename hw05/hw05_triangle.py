for i in range(3):
    for j in range(2-i):
        print(" ",end="")
    for j in range(2*(i+1)-1):
        print("*",end="")
    print()
