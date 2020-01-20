class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if B in A:
            return 1
        else:
            l1 = len(A)
            l2 = len(B)
            max = 2 * l1 + l2
            count = 1
            C = ""
            while len(C) < max:
                count += 1
                C = A * count          
                if B in C:
                    return count
            return -1
            
    
s = Solution()
print(s.repeatedStringMatch("abcd", "cdabcdab"))