class Solution:
    def maxDepth(self, s: str) -> int:
        depth = []
        max_depth = 0
        for i in s:
            if i == "(":
                depth.append("(")
            elif i == ")":
                depth.pop()
            max_depth = max(max_depth, len(depth))
        return max_depth


s = Solution()
print(s.maxDepth("(1+(2*3)+((8)/4))+1"))
