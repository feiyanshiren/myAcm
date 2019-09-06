class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
    
s = Solution()
print(s.countSegments("Hello, my name is John"))
print(s.countSegments(", , , ,   a, eaefa"))
print(s.countSegments("                "))
