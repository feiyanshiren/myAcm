from typing import List
import collections
import itertools

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        ll = len(arr)
        for i in range(m):
            a = []
            for j in range(i, ll, m):
                if j + m <= ll:
                    a.append(tuple(arr[j: j + m]))
            c = 1
            j = 1
            b = a[0]
            while c < len(a):
                if b == a[c]:
                    j += 1
                    if j >= k:
                        return True
                else:
                    b = a[c]
                    j = 1
                c += 1
        return False                
                

# 使用数组和元组分组后在计算连续次数

s = Solution()
print(s.containsPattern([1,2,4,4,4,4], 1, 3))
print(s.containsPattern([1,2,1,2,1,1,1,3], 2, 2))
print(s.containsPattern([1,2,1,2,1,3], 2, 3))
print(s.containsPattern([99,9], 1, 3))