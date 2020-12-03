"""
709.
转换成小写字母
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
判断
65
到
90
加
32

"""


class Solution:
    def toLowerCase(self, str: str) -> str:
        s = ""
        for i in str:
            a = ord(i)
            if a >= 65 and a <= 90:
                a += 32
            s += chr(a)
        return s


