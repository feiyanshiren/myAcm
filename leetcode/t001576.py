class Solution:
    def modifyString(self, s: str) -> str:
        k = "abcdefghijklmnopqrstuvwxyz"
        list_s = list(s)
        ll = len(list_s)
        for i in range(ll):
            if list_s[i] == "?":
                left = ""
                right = ""
                if i != 0:
                    left = list_s[i - 1]
                if i != ll - 1:
                    right = list_s[i + 1]
                for j in k:
                    if j != left and j != right:
                        list_s[i] = j
                        break
        return "".join(list_s)


s = Solution()
print(s.modifyString("?zs"))
