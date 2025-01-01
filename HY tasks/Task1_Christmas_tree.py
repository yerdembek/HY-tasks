hight = 10

for i in range(hight):
    for j in range(hight - i - 1):
        print (" ", end="")

    for j in range(2 * i + 1):
        print ("*", end="")
    print()
