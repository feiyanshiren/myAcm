


class Solution:

    def buddyStrings(self, A: str, B: str) -> bool:
        l1 = len(A)
        l2 = len(B)
        if l1 < 2 or l2 < 2 or l1 != l2:
            return False
        if A == B:
            a1 = list(A)
            for i in a1:
                if a1.count(i) > 1:
                    return True
                else:
                    return False
        a = []
        b = []
        for i in range(l1):
            if A[i] != B[i]:
                a.append(A[i])
                b.append(B[i])
        if len(a) != 2 or len(b) != 2:
            return False
        a[0], a[1] = a[1], a[0]
        if a == b:
            return True
        else:
            return False


# ```
# ---
#
# 859.
# 亲密字符串 - -2
#
# 给定两个由小写字母构成的字符串
# A
# 和
# B ，只要我们可以通过交换
# A
# 中的两个字母得到与
# B
# 相等的结果，就返回
# true ；否则返回
# false 。
#
#
#
# 示例
# 1：
#
# 输入： A = "ab", B = "ba"
# 输出： true
#
# 示例
# 2：
#
# 输入： A = "ab", B = "ab"
# 输出： false
#
# 示例
# 3:
#
# 输入： A = "aa", B = "aa"
# 输出： true
#
# 示例
# 4：
#
# 输入： A = "aaaaaaabc", B = "aaaaaaacb"
# 输出： true
#
# 示例
# 5：
#
# 输入： A = "", B = "aa"
# 输出： false
#
# 提示：
#
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A
# 和
# B
# 仅由小写字母构成。
#
# 解：
# 字符串长度不相等, 直接返回false
# 字符串相等的时候, 只要有重复的元素就返回true
# A, B字符串有不相等的两个地方, 需要查看它们交换后是否相等即可.
# 使用zip
# ```


class Solution(object):

    def buddyStrings(self, A, B):
        # 长度不同直接false
        if len(A) != len(B):
            return False
        # 由于必须交换一次，在相同的情况下，交换相同的字符
        if A == B and len(set(A)) < len(A):
            return True
        # 使用 zip 进行匹配对比，挑出不同的字符对
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        # 对数只能为2，并且对称，如 (a,b)与(b,a)
        return len(dif) == 2 and dif[0] == dif[1][::-1]


