for t in range(int(input())):
    h = int(input())
    x = 0 
    while h > 10:
        h -= 5
        x += 1
    print(x + 1)