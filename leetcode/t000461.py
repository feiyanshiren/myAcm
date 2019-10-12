class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x)[2:]
        b = bin(y)[2:]
        l1 = len(a)
        l2 = len(b)
        d = l1
        if l1 <= l2:
            c = l2 - l1
            a = "0" * c + a
            d = l2
        else:
            c = l1 - l2
            b = "0" * c + b
        e = 0
        for i in range(d):
            if a[i] != b[i]:
                e += 1
        return(e)
    

s = Solution()
print(s.hammingDistance(1, 4))