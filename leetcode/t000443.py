from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        m = [chars[0]]
        d = 1
        for j in range(1, len(chars)):
            i = chars[j]
            if m[-1] == i:
                d += 1
            else:
                if d > 1:
                    sd = str(d)
                    for K in range(len(sd)):
                        m.append(sd[K])
                    d = 1
                m.append(i)
        if d > 1:
            sd = str(d)
            for i in range(len(sd)):
                m.append(sd[i])
        chars = m
        # print(chars)
        d = len(chars)
        return d
    
s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))
print(s.compress(["a"]))
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(s.compress(["a","a","a","b","b","a","a"]))