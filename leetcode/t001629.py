from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        map_rel = {}
        releaseTimes.insert(0, 0)
        for i in range(len(releaseTimes)):
            s = releaseTimes[i] - releaseTimes[i - 1]
            map_rel[keysPressed[i - 1]] = max(map_rel.get(keysPressed[i - 1], 0), s)
        max_c = max(map_rel.values())
        mm = [k for k, v in map_rel.items() if v == max_c]
        mm.sort()
        return mm[-1]


s = Solution()
print(s.slowestKey([9, 29, 49, 50], "cbcd"))
print(s.slowestKey([12,23,36,46,62], "spuda"))

