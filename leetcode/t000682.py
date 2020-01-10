from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        i_sum = 0
        i_len = len(ops)
        i = 0
        while i < i_len:
            s_op = ops[i]
            if s_op == "C":
                if i - 1 >= 0:
                    s_op_1 = ops[i - 1]
                    i_sum -= int(s_op_1)
                    del ops[i - 1]
                    del ops[i - 1]
                    i -= 2
                    i_len -= 2
            elif s_op == "D":
                if i - 1 >= 0:
                    s_op_1 = ops[i - 1]
                    s_op_t = str(2 * int(s_op_1))
                    ops[i] = s_op_t
                    i_sum += 2 * int(s_op_1)
            elif s_op == "+":
                if i - 1 >= 0:
                    s_op_1 = ops[i - 1]
                    ops[i] = s_op_1
                    i_sum += int(s_op_1)
                if i - 2 >= 0:
                    s_op_2 = ops[i - 2]
                    ops[i] = int(ops[i]) + int(s_op_2)
                    i_sum += int(s_op_2)
            else:
                i_sum += int(s_op)
            i += 1
        return i_sum
    

s = Solution()
print(s.calPoints(["5","2","C","D","+"]))
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))