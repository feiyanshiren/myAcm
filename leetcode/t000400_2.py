class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while n > i * (pow(10, i - 1)) * 9:
            n -= i * (pow(10, i - 1)) * 9
            i += 1
        a = (n-1) // i + pow(10, i - 1)
        s = str(a)
        k = n % i
        if k == 0:
            k = i
        return int(s[k - 1])
            
            
    
s = Solution()
print(s.findNthDigit(3))
print(s.findNthDigit(11))
print(s.findNthDigit(21479834567))

"""
1-9有9个数，10-99有20X9个数字，100-999有300X9个数字，1000-9999有4000X9个数字；以此类推；
设置一个标志位i，每一个区间都有固定的标志位，例如1-9是1，10--99是2，以此类推；然后用n减去每个区间的值，知道确定n在哪个区间；
在得到区间中确定的数字，将其变为string型，然后就可以得到确定的数字。
"""
