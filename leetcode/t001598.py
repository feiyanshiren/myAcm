from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if i == "./":
                pass
            elif i == "../":
                try:
                    stack.pop()
                except:
                    pass
            else:
                stack.append(i)
        return len(stack)


s = Solution()
print(s.minOperations(["d1/", "d2/", "../", "d21/", "./"]))
print(s.minOperations(["d1/","d2/","./","d3/","../","d31/"]))
print(s.minOperations( ["d1/","../","../","../"]))
