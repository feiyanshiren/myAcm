for T in range(int(input())):
    s = input().split()
    print(sum(int(i) for i in s[0])+sum(int(i) for i in s[1]))