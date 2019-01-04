import math 

def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 

def isFibonacci(n): 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
    
    
while 1:
    s = int(input())
    if s == 0:
        break
    else:
        if isFibonacci(s):
            print("YES")
        else:
            print("NO")