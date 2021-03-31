class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        li = []
        for i in range(1, n + 1):
            a3 = i % 3
            a5 = i % 5
            if a3 == 0 and a5 == 0:
                li.append("FizzBuzz")
            elif a3 == 0 and a5 != 0:
                li.append("Fizz")
            elif a3 != 0 and a5 == 0:
                li.append("Buzz")
            else:
                li.append(str(i))
        return li
    
s = Solution()
print(s.fizzBuzz(15000))