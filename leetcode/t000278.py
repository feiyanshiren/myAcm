# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version <= 3:
        return False
    else:
        return True

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [i for i in range(1, n + 1)]
        k = n // 2
        m = n
        while len(a) > 0:
            if isBadVersion(a[k]):
                m = a[k]
                a = a[:k]
            else:
                a = a[k + 1:]
            k = len(a) // 2
        return m
            
                
                
            
        
            
    

s = Solution()
print(s.firstBadVersion(5))
        