from typing import List
import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        b = int(math.sqrt(area))
        while area % b != 0:
            if b == 1:
                return [area, 1]
            else:
                b -= 1
        return [area // b, b]
                    
    
    
s = Solution()
print(s.constructRectangle(4))
print(s.constructRectangle(9999999999))