from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ll = len(arr)
        res = 0
        for i in range(1, ll + 1, 2):
            c = 0
            for j in range(ll - i + 1):
                c += sum(arr[j: j + i])
            res += c
        return res



s = Solution()
print(s.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
print(s.sumOddLengthSubarrays([1, 2]))
print(s.sumOddLengthSubarrays([10, 11, 12]))
