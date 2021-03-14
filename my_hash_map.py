class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 100
        self.hashmap = [[]] * self.length

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        p = key % self.length
        for i in range(len(self.hashmap[p])):
            if self.hashmap[p][i][0] == key:
                self.hashmap[p][i][1] = value
                return
        self.hashmap[p].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        p = key % self.length
        for k, v in self.hashmap[p]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        p = key % self.length
        for k, v in self.hashmap[p][:]:
            if k == key:
                self.hashmap[p].remove([k, v])


if __name__ == "__main__":
    # Your MyHashMap object will be instantiated and called as such:
    obj = MyHashMap()
    obj.put(1, 1)
    param_2 = obj.get(1)
    obj.put(2, 2)
    obj.remove(1)
