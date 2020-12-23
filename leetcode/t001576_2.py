class Solution:
    def modifyString(self, s: str) -> str:
        list_s = list(" " + s + " ")
        k = "abcdefghijklmnopqrstuvwxyz"
        for i in range(1, len(list_s) - 1):
            if list_s[i] == "?":
                for j in k:
                    if j != list_s[i - 1] and j != list_s[i + 1]:
                        list_s[i] = j
                        break
        return "".join(list_s).strip()


s = Solution()
print(s.modifyString("?zs"))
print(ord("a"))
print(ord("z"))
