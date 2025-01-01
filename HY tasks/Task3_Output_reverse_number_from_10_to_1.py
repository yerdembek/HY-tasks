start = 1
stop = 2
current_num = 2

for row in range(1, 5):
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")

    start = stop
    stop += row + 1
    current_num = stop