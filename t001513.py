"""
a = []
for i in range(1000):
    g =  i ** 4
    u = (i + 1) ** 4
    x = (i + 2) ** 4
    print("%d:%d" % (i, i ** 4))
    if x == g + u:
        print("yes-%d:%d:%d" % (i, i + 1, i + 2))
    else:
        print("no")
"""
"""
https://zhuanlan.zhihu.com/p/60463619
继续推广，到n阶形式会怎样呢～～


a^n+b^n=c^n

a^n=c^n-b^n

=（c-b）（c^（n-1）+c^（n-2）b+c^（n-3）b^2+……+cb^（n-2）+b^（n-1））

令c-b=1，则

a^n=（（b+1）^（n-1）+（b+1）^（n-2）b+（b+1）^（n-3）b^2+……+（b+1）b^（n-2）+b^（n-1））

你妹，这TM怎么解。

不过仔细观察一下，

右边的常数项是1，移项到左边就是a^n-1=（a-1）（a^（n-1）+a^（n-2）+…+a+1）两项互质但都能被n整除。

右边剩下的就是b（b【n-2】）。其中b【n-2】是b的n-2阶多项式。有足够耐心的话应该可以求出来，但我实在是懒得求了～～不过大概可以看出，有公因式n，而且很可能是可以因式分解的。

因为都是整数而且互质，所以我们可以只考虑一种情形：

a-1=b，a【n-1】=b【n-2】

两个方程两个未知数，可以解出来。

有n-1组根，但绝大多数根连实数都不是，更不要说整数了。

可以用特殊值法凑出一个解：a=1，b=0，c=1；另一个解a=-1，b=0，c=-1。其它的解应该可以证明没有整数。其实它们是可以以f（n）的形式解出来的。

这样似乎可以证明费马大定理。不过过程中存在逻辑链缺失。毕竟，完整的证明要二十多页纸。不过感觉上证明这个定理似乎有更简单的方法。不过谁知道呢～～
"""

print("NO")