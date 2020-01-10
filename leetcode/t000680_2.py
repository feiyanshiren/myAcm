class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = len(s)
        left = 0
        right = l - 1
        if_del = 0
        res1 = True
        res2 = True
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if if_del == 0:
                    left += 1
                    if left == right:
                        break
                    if_del = 1
                else:
                    res1 = False
                    break
        left = 0
        right = l - 1
        if_del = 0
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if if_del == 0:
                    right -= 1
                    if left == right:
                        break
                    if_del = 1
                else:
                    res2 = False
                    break
        return res1 | res2



s = Solution()
# print(s.validPalindrome("aba"))
# print(s.validPalindrome("abca"))
# print(s.validPalindrome("aaaaaa"))
print(s.validPalindrome("abababababababababababababababababababac"))
# print(s.validPalindrome("abcd"))
# print(s.validPalindrome("cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu"))
