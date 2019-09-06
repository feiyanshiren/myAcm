class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        li = []
        for i in range(1, n + 1):
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                 s += "Buzz"
            if s == "":
                s += str(i)
            li.append(s)
        return li
    
s = Solution()
print(s.fizzBuzz(15000))