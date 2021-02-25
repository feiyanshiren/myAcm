from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        l1 = len(arr)
        for i in pieces:
            try:
                k = arr.index(i[0])
                ll = len(i)
                for j in range(1, ll):
                    k += 1
                    if k >= l1:
                        return False
                    if arr[k] != i[j]:
                        return False
            except ValueError as e:
                return False
        return True


s = Solution()
print(s.canFormArray([85], [[85]]))
print(s.canFormArray([15,88], [[88],[15]]))
print(s.canFormArray([49,18,16], [[16,18,49]]))
print(s.canFormArray([91,4,64,78], [[78],[4,64],[91]]))
print(s.canFormArray([1,3,5,7], [[2,4,6,8]]))
print(s.canFormArray([4,5], [[45],[4]]))