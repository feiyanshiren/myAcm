class Solution:
    def getRow(self, rowIndex):
    # def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if rowIndex <= 0:
            return [1]
        res = []
        for i in range(1, rowIndex + 2):
            res.append([1 for j in range(i)])
        for i in range(rowIndex):
            a = res[i]
            l = len(a)
            if l > 1:
                for j in range(l - 1):
                    s = a[j] + a[j + 1]
                    res[i + 1][j + 1] = s
        return res[rowIndex]


s = Solution()
print(s.getRow(0))
print(s.getRow(33))

