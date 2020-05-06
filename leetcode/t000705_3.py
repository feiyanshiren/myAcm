class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = [0 for i in range(1563)]
        

    def add(self, key: int) -> None:
        yu  = key // 64
        self.nums[yu] |= 1 << key
        

    def remove(self, key: int) -> None:
        yu  = key // 64
        k = 1 << key
        if self.nums[yu] & k == k:
            self.nums[yu] ^= 1 << key
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        yu  = key // 64
        k = 1 << key
        return self.nums[yu] & k == k
        


# Your MyHashSet object will be instantiated and called as such:
key = 78
key2 = 79
obj = MyHashSet()
obj.add(key)
obj.add(key2)
obj.remove(key)
param_3 = obj.contains(key)
print(param_3)
print(obj.contains(key2))