from typing import List
import math


class MaxHeap:
    def __init__(self):
        self.nums = []

    def father(self, pos: int):
        """Find `pos` element's father element's pos."""
        return math.floor((pos - 1) / 2)

    def left_child(self, pos: int):
        """Find `pos` element's left child element's pos."""
        return (pos + 1) * 2 - 1

    def right_child(self, pos: int):
        """Find `pos` element's right child element's pos."""
        return (pos + 1) * 2

    def insert(self, num: int):
        """Insert `num` to max heap."""
        self.nums.append(num)
        p = len(self.nums)
        while num > self.nums[self.father(p)]:
            self.nums[p] = self.nums[self.father(p)]
            self.nums[self.father(p)] = num
            p = self.father(p)

    def pop(self):
        """Pop max element of the max heap."""
        num = self.nums[0]
        self.nums[0] = self.nums[-1]
        self.down(0)

    def down(self, pos: int, last_pos=None):
        """Sink `pos` element down to the right place."""
        if not last_pos:
            last_pos = len(self.nums)
        def find_max_pos(pos: int):
            left, right = self.left_child(pos), self.right_child(pos)
            if left < last_pos and right < last_pos:
                max_pos = left if self.nums[left] > self.nums[right] else right
            elif left < last_pos:
                max_pos = left
            elif right < last_pos:
                max_pos = right
            else:
                max_pos = pos
            return max_pos
        max_pos = find_max_pos(pos)
        while self.nums[pos] < self.nums[max_pos]:
            t = self.nums[pos]
            self.nums[pos] = self.nums[max_pos]
            self.nums[max_pos] = t
            pos = max_pos
            max_pos = find_max_pos(pos)

    def sort(self):
        # after sort, not a max heap anymore
        def swap(pos_a, pos_b):
            t = self.nums[pos_a]
            self.nums[pos_a] = self.nums[pos_b]
            self.nums[pos_b] = t

        p = len(self.nums) - 1
        while p > 0:
            swap(0, p)
            self.down(0, p)
            p -= 1


    def __str__(self):
        return str(self.nums)


def construct_max_heap(nums: List[int]):
    max_heap = MaxHeap()
    for n in nums:
        max_heap.insert(n)
    return max_heap


def construct_max_heap_inplace(nums: List[int]):
    max_heap = MaxHeap()
    max_heap.nums = nums
    for i in range(len(nums) // 2 - 1, -1, -1):
        max_heap.down(i)
    return max_heap


if __name__ == "__main__":
    nums = [3, 9, 12, 6, 1, 4, 5]
    max_heap = construct_max_heap_inplace(nums)
    print(max_heap)
    max_heap.sort()
    print(max_heap)
