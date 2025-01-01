hight = 10

for i in range(hight):
    for j in range(hight - i - 1):
        print (" ", end="")
    if i == 0:
        print (2025, end="")
    else:
        for j in range(2 * i + 1):
            print ("*", end="")
    print()
