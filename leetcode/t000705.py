class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = set()
        

    def add(self, key: int) -> None:
        self.nums.add(key)
        

    def remove(self, key: int) -> None:
        self.nums.remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.nums
        


# Your MyHashSet object will be instantiated and called as such:
key = 1
obj = MyHashSet()
obj.add(key)
# obj.remove(key)
param_3 = obj.contains(key)
print(param_3)