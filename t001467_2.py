n=int(input())
while n:
    n-=1
    num=int(input())
    for i in range(num):
        print(' '*i+'*'*((num-i)*2-1),end='')
        print()
    for i in range(num-1):
        print(' '*(num-2-i)+'*'*(2*i+3),end='')
        print()
    print()