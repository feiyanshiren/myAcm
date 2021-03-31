# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version == 3:
        return False
    else:
        return True

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(1, n + 1):
            if isBadVersion(i):
                return i
        return n + 1
                
                
            
        
            
    

s = Solution()
print(s.firstBadVersion(5))
        