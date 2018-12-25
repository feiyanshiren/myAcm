class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        z = 0
        m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        le = len(s)
        while i != le:
            if (i + 1) < le and m[s[i]] < m[s[i + 1]]:
                z = z + m[s[i + 1]] - m[s[i]]
                i += 2
            else:
                z = z + m[s[i]]
                i += 1
        return z
    
s = Solution()
print(s.romanToInt("MCMXCIV"))