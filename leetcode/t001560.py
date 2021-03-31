from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        mm = {i: 0 for i in range(1, n + 1)}
        mm[rounds[0]] += 1
        for i in range(0, len(rounds) - 1):
            s1 = rounds[i]
            s2 = rounds[i + 1]
            if s2 >= s1:
                for k in range(s1 + 1, s2 + 1):
                    mm[k] += 1
            else:
                for k in range(s1 + 1, n + 1):
                    mm[k] += 1
                for k in range(1, s2 + 1):
                        mm[k] += 1
        the_max = max(mm.values())
        res = []
        for i in range(1, n + 1):
            if mm[i] == the_max:
                res.append(i)
        return res
            

# 解 模拟

s = Solution()
print(s.mostVisited(4, [1, 3, 1, 2]))
print(s.mostVisited(2, [2,1,2,1,2,1,2,1,2]))
print(s.mostVisited(7, [1,3,5,7]))
