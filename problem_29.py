for i in range(100, 1001):
    s = str(i)
    if sum([int(d)**3 for d in s]) == i:
        print(i)
