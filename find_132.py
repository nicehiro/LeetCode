from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        return self.method2(nums)

    def method1(self, nums):
        n = len(nums)
        numi = nums[0]
        for j in range(1, n):
            for k in range(j, n):
                if nums[k] > numi and nums[k] < nums[j]:
                    return True
            numi = min(numi, nums[j])
        return False

    def method2(self, nums):
        """单调栈找小于某个数的最大数。"""
        n = len(nums)
        min_i = [float("inf")] * n
        for i in range(1, n):
            min_i[i] = min(min_i[i - 1], nums[i - 1])

        stack = []
        for j in range(n - 1, 0, -1):
            while stack and stack[-1] < nums[j]:
                numk = stack.pop()
                if numk > min_i[j]:
                    return True
            stack.append(nums[j])
        return False
