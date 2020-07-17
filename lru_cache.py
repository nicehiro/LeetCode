class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.recents = []
        self.last = -1

    def get(self, key: int) -> int:
        if key in self.cache:
            self.__visit(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.__visit(key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.__visit(key)

    def __visit(self, key):
        if self.last != key:
            if key in self.recents:
                self.recents.remove(key)
            self.recents.append(key)
        if len(self.recents) > self.capacity:
            old = self.recents.pop(0)
            self.cache.pop(old, None)
        self.last = key


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.__move_to_head(node)
            return node.value
        return -1

    def __move_to_head(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def __insert_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def __remove_from_tail(self):
        t = self.tail.prev
        t.prev.next = self.tail
        self.tail.prev = t.prev
        self.cache.pop(t.key)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.__move_to_head(node)
        else:
            node = DLinkedNode(key, value)
            self.__insert_to_head(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                self.__remove_from_tail()


if __name__ == '__main__':
    lru = LRUCache2(10)
    # lru.put(1, 1)
    # lru.put(2, 2)
    # print(lru.get(1))
    # lru.put(3, 3)
    # print(lru.get(2))
    # lru.put(4, 4)
    # print(lru.get(1))
    # print(lru.get(3))
    # print(lru.get(4))

    lru.put(10, 13)
    lru.put(3, 17)
    lru.put(6, 11)
    lru.put(10, 5)
    lru.put(9, 10)
    print(lru.get(13))
    lru.put(2, 19)
    print(lru.get(2))
    print(lru.get(3))
    lru.put(5, 25)
    print(lru.get(8))
    lru.put(9, 22)
    lru.put(5, 5)
    lru.put(1, 30)
    print(lru.get(11))
    lru.put(9, 12)
    print(lru.get(7))
    print(lru.get(5))
    print(lru.get(8))
    print(lru.get(9))
    lru.put(4, 30)
    lru.put(9, 3)
    print(lru.get(9))
    print(lru.get(10))

    # lru.put(2, 1)
    # lru.put(1, 1)
    # lru.put(2, 3)
    # lru.put(4, 1)
    # print(lru.get(1))
    # print(lru.get(2))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
