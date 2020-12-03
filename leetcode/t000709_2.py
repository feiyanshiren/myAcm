"""
709.
转换成小写字母 - -2
题目描述

实现函数
ToLowerCase()，该函数接收一个字符串参数
str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。



示例
1：

输入: "Hello"
输出: "hello"

示例
2：

输入: "here"
输出: "here"

示例
3：

输入: "LOVELY"
输出: "lovely"

解：
使用ascii
使用位运算
大写变小写、小写变大写: ASCII码 ^= 32
大写变小写、小写变小写: ASCII码 |= 32
小写变大写、大写变大写: ASCII码 &= -33
"""


class Solution:
    def toLowerCase(self, str: str) -> str:
        s = ""
        for i in str:
            a = ord(i)
            a |= 32
            s += chr(a)
        return s