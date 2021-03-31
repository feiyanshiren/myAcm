from typing import List


class Solution(object):
    def canFormArray(self, arr, pieces):
        for i in pieces:
            if i[0] not in  arr:
                return False
            elif i != arr[arr.index(i[0]):arr.index(i[0])+len(i)] :
                return False
        return True




s = Solution()
print(s.canFormArray([85], [[85]]))
print(s.canFormArray([15,88], [[88],[15]]))
print(s.canFormArray([49,18,16], [[16,18,49]]))
print(s.canFormArray([91,4,64,78], [[78],[4,64],[91]]))
print(s.canFormArray([1,3,5,7], [[2,4,6,8]]))
print(s.canFormArray([4,5], [[45],[4]]))
print(s.canFormArray([1,2,3], [[2],[1,3]]))