class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._data.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self._data.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self._data) != 0:
            return self._data[-1]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self._data) != 0:
            return min(self._data)
        else:
            return None
        

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)
