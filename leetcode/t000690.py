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
        f = None
        for i in employees:
            if i.id == id:
                f = i
                break
        d = f.subordinates[:]
        h = f.importance
        while len(d) != 0:
            a = d.pop()
            for i in employees:
                if i.id == a:
                    h += i.importance
                    if i.subordinates:
                        d += i.subordinates
        return h
                
        
    
s = Solution()

employees = [Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])]

print(s.getImportance(employees, 1))