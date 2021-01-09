from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return self.rotate_2(nums, k)

    def rotate_1(self, nums, k):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not nums:
            return
        n = len(nums)
        i = 0
        t = nums[i]
        visited = set()
        while len(visited) < n:
            while i in visited:
                i += 1
                t = nums[i]
            visited.add(i)
            j = (i + k) % n
            a = nums[j]
            nums[j] = t
            t = a
            i = j

    def rotate_2(self, nums, k):
        """
        Time Complexity: O(n)
        但是其计算 lcm 时耗费的时间明显要比hash 长
        Space Complexity: O(1)
        """
        if not nums or k == 0:
            return
        n = len(nums)
        count = 0
        t = self.lcm(n, k) // k
        v = 0
        while count < n:
            i = v
            m = nums[i]
            for _ in range(t):
                j = (i + k) % n
                a = nums[j]
                nums[j] = m
                m = a
                i = j
                count += 1
            v += 1

    def lcm(self, a, b):
        m, n = max(a, b), min(a, b)
        times = 1
        while True:
            t = m * times
            if t % n == 0:
                return t
            times += 1
