from typing import List


# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        map_e = {i.id:i for i in employees}
        d = map_e.get(id).subordinates[:]
        h = map_e.get(id).importance
        while len(d) != 0:
            a = d.pop()
            h += map_e.get(a).importance
            if map_e.get(a).subordinates:
                d += map_e.get(a).subordinates
        return h
        
    
s = Solution()

employees = [Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])]

print(s.getImportance(employees, 1))