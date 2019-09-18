from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 1
        ll = len(chars)
        d = 1
        while right < ll:
            s1 = chars[left]
            s2 = chars[right]
            if s1 != s2:
                if d > 1:
                    sd = str(d)
                    lsd = len(sd)
                    for i in range(lsd):
                        chars.insert(right + i, sd[i])
                    for i in range(right - 1, left, -1):
                        chars.pop(i)
                    ll = len(chars)
                    left += lsd + 1
                    right = left + 1
                    d = 1
                else:
                    left += 1
                    right += 1 
            else:
                d += 1
                right += 1
        if d > 1:
            for i in range(d - 1):
                chars.pop()
            sd = str(d)
            lsd = len(sd)
            for i in range(lsd):
                chars.append(sd[i])
        return len(chars)
    
s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))
print(s.compress(["a"]))
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(s.compress([]))
print(s.compress(["a","a","a","b","b","a","a"]))