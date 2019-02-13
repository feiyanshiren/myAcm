class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, numRows + 1):
            res.append([1 for j in range(i)])
        for i in range(numRows - 1):
            a = res[i]
            l = len(a)
            if l > 1:
                for j in range(l - 1):
                    s = a[j] + a[j + 1]
                    res[i + 1][j + 1] = s
        return res

s = Solution()
print(s.generate(0))
print(s.generate(1))
print(s.generate(2))
print(s.generate(3))
print(s.generate(4))
print(s.generate(5))
print(s.generate(10))
