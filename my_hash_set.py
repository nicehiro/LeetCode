class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 100
        self.hashset = [[]] * self.length

    def add(self, key: int) -> None:
        p = key % self.length
        if not self.contains(key):
            self.hashset[p].append(key)

    def remove(self, key: int) -> None:
        p = key % self.length
        if self.contains(key):
            self.hashset[p].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        p = key % self.length
        for k in self.hashset[p]:
            if k == key:
                return True
        return False


if __name__ == "__main__":
    # Your MyHashSet object will be instantiated and called as such:
    obj = MyHashSet()
    obj.add(key)
    obj.remove(key)
    param_3 = obj.contains(key)
