from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))


s = Solution()
print(s.plusOne([1,2,3]))