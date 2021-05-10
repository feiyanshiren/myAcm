import math
def is_prime(val):
    if val < 2:
        return 0
    k = int(math.sqrt(val))
    for i in range(2, k + 1):
        if val % i == 0:
            return 0
    return 1

for T in range(int(input())):
    N = int(input())
    if is_prime(N):
        print("YES")
    else:
        print("NO")