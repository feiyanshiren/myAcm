from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        c = 0
        l = 0
        l1 = len(grid)
        l2 = 0
        if l1 != 0:
            l2 = len(grid[0])
        else:
            return 0
        for i in range(l1):
            for j in range(l2):
                a = grid[i][j]
                if a == 1:
                    c += 1
                    l += self.isP(grid, i, j)
        return(c * 4 - l) 
                
    def isP(self, grid, i, j):
        l = 0
        if i > 0:
            if grid[i - 1][j] == 1:
                l += 1
        if j > 0:
            if grid[i][j - 1] == 1:
                l += 1
        return l * 2
        
    
s = Solution()
print(s.islandPerimeter(
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))