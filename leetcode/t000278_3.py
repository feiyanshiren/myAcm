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
        l = 1
        h = n
        m = (h + l) // 2
        while l < h:
            if not isBadVersion(m):
                l = m + 1
            else:
                h = m
            m = (h + l) // 2
        return l
            
                
                
            
        
            
    

s = Solution()
print(s.firstBadVersion(5))
        