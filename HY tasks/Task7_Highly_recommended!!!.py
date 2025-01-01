height = 7
symbol = ord(input("Enter the starting character: "))

print("\n\tHappy New Year!")
x =(2 * height) - 2
for i in range(height):
    print(" " * x, end="")
    x -= 1
    for j in range(i + 1):
        print(chr(symbol), end=" ")
        symbol += 1
    print()

print("\n\tWish you all the Best")