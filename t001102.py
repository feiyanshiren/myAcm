try:
    while 1:
        n = int(input())
        if (n - 2) % 4 == 0:
            print("Yes")
        else:
            print("No")
except EOFError:
    pass
