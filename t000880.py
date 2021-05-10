for N in range(int(input())):
    m = int(input())
    for i in range(1, m + 2):
        z = 65
        for j in range(1, m + 2 - i): print(" ", end="")
        for k in range(1, i + 1):
            print(chr(z), end="")
            z += 1
        for k in range(i + 1, 2 * i):
            print(chr(z - 2), end="")
            z -= 1
        print()
    for i in range(m, -1, -1):
        z = 65
        for j in range(m - i, -1, -1): print(" ", end="")
        for k in range(i -1, -1, -1):
            print(chr(z), end="")
            z += 1
        for k in range(2 * i - 3, i - 2, -1):
            print(chr(z - 2), end="")
            z -= 1
        print()
        
    