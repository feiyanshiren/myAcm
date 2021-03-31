class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.helper) == 0:
            self.helper.append(x)
        else:
            if x <= self.helper[-1]:
                self.helper.append(x)
                
            
        
        

    def pop(self):
        """
        :rtype: None
        """
        num = self.stack.pop()
        if len(self.helper)>0 and num  == self.helper[-1]:
            self.helper.pop()
        
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0: return 0
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.helper) == 0: return 0
        return self.helper[-1]
        

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
