from typing import List

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        first = rounds[0]
        last = rounds[-1]
        if last==first:
            return [first]
        elif first<last :
            return [ i for i in range(first,last+1)]
        else:
            return [i for i in range(1,last+1)]+[ i for i in range(first,n+1)]

# 每次走过一圈时。大家走的次数都是一样的，随意只关注最后一圈走过了多少就行，最后一圈的起点就是首元素，结尾就是表示最后一圈的终点，判断一下起终点关系就