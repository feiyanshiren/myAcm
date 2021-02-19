from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_k = ""
        max_v = 0
        releaseTimes.insert(0, 0)
        for i in range(1, len(releaseTimes)):
            s = releaseTimes[i] - releaseTimes[i - 1]
            if s > max_v:
                max_v = s
                max_k = keysPressed[i - 1]
            elif s == max_v:
                if keysPressed[i - 1] > max_k:
                    max_k = keysPressed[i - 1]
        print(max_v)
        return max_k


s = Solution()
print(s.slowestKey([9, 29, 49, 50], "cbcd"))
print(s.slowestKey([12, 23, 36, 46, 62], "spuda"))
