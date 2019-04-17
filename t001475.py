for T in range(int(input())):
    n = int(input())
    j = []
    for i in range(n):
        s = input()
        s += s[::-1]
        j.append(s)
    j += j[::-1]
    for i in j:
        print(i)
        