# 717. 1比特与2比特字符
# 题目描述
#
#
# 有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
#
# 现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。
#
# 示例 1:
#
# 输入:
# bits = [1, 0, 0]
# 输出: True
# 解释:
# 唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
#
# 示例 2:
#
# 输入:
# bits = [1, 1, 1, 0]
# 输出: False
# 解释:
# 唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。
#
# 注意:
#
#     1 <= len(bits) <= 1000.
#     bits[i] 总是0 或 1.
#
# 解：
# 判断后面连续11,基本上的测试错误弄出来的.
#
# ```
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        l = len(bits)
        if l == 1:
            if bits[l - 1] == 1:
                return False
            else:
                return True
        elif l == 2:
            if bits[l - 1] == 0 and bits[l - 2] == 0:
                return True
            else:
                return False
        else:
            if bits[l - 1] == 0:
                if bits[l - 2] == 0:
                    return True
                else:
                    c = 0
                    for i in range(l - 2, -1, -1):
                        a = bits[i]
                        if a == 1:
                            c += 1
                        else:
                            break
                    if c % 2 == 0:
                        return True
                    else:
                        return False
            else:
                return False