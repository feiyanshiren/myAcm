class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str1 = list(str.split())
        return list(map(pattern.index, pattern)) == list(map(str1.index, str1))
            
    

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("abba", "dog cat cat fish"))
#print(s.wordPattern("aaaa", "dog cat cat dog"))
#print(s.wordPattern("abba", "dog dog dog dog"))
print(s.wordPattern("abc", "b c a"))