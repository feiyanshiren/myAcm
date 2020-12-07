# 733. 图像渲染
# 题目描述
#
#
# 有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。
#
# 给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。
#
# 为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。
#
# 最后返回经过上色渲染后的图像。
#
# 示例 1:
#
# 输入:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# 输出: [[2,2,2],[2,2,0],[2,0,1]]
# 解析:
# 在图像的正中间，(坐标(sr,sc)=(1,1)),
# 在路径上所有符合条件的像素点的颜色都被更改成2。
# 注意，右下角的像素没有更改为2，
# 因为它不是在上下左右四个方向上与初始点相连的像素点。
#
# 注意:
#
#     image 和 image[0] 的长度在范围 [1, 50] 内。
#     给出的初始点将满足 0 <= sr < image.length 和 0 <= sc < image[0].length。
#     image[i][j] 和 newColor 表示的颜色值在范围 [0, 65535]内。
#
# 解：
# 题目大意： 首先，你别看输入输出样例。越看越懵，， 有一幅图画，上面有各种颜色（用数字0-65535表示不同颜色）。像素就是二维坐标。通过坐标可以知道该像素是啥颜色。然后给你一个坐标（sr,sc）和一个替换颜色newColor。 （sr,sc）本身的颜色我们记为color. 要求你从（sr,sc）开始，遍历上下左右相邻的像素点，如果相邻的像素点的颜色是color,则把他改为替换颜色newColor；如果该点的颜色和替换颜色newColor一样，不在遍历他的相邻像素。循环。。。。
#
#
# ```
class Solution(object):
    def f(self, x, y, image, old_color, newColor, len_w, len_l):
        if image[x][y] == old_color:
            image[x][y] = newColor
            if x >= 1:
                self.f(x - 1, y, image, old_color, newColor, len_w, len_l)
            if x < len_w - 1:
                self.f(x + 1, y, image, old_color, newColor, len_w, len_l)
            if y >= 1:
                self.f(x, y - 1, image, old_color, newColor, len_w, len_l)
            if y < len_l - 1:
                self.f(x, y + 1, image, old_color, newColor, len_w, len_l)

    def floodFill(self, image, sr, sc, newColor):
        old_color = image[sr][sc]
        if old_color == newColor:
            return image
        len_w = len(image)
        len_l = len(image[0])
        self.f(sr, sc, image, old_color, newColor, len_w, len_l)
        return image