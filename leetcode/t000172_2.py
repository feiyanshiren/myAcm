class Solution:
    def trailingZeroes(self, n: int) -> int:
        c = 0
        while n >= 5:
            n = n // 5
            c += n
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
        