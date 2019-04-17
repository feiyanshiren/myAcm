import math

class Solution:
    def trailingZeroes(self, n: int) -> int:
        j = str(math.factorial(n))
        c = 0
        for i in range(len(j) - 1, -1, -1):
            if j[i] == "0":
                c += 1
            else:
                break
        return c

 
s = Solution()
o = 0
for i in range(9551):
    k = s.trailingZeroes(i)
    if k == o:
        print("%d:%d" % (i, k), end=" ")
    else:
        print()
        print("%d:%d" % (i, k), end=" ")
    o = k
        