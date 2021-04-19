from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i, j = 0, n - 1
        while i <= j:
            while i < n and nums[i] != val:
                i += 1
            while j >= 0 and nums[j] == val:
                j -= 1
            if i >= n or j < 0:
                break
            if i < j:
                a = nums[i]
                nums[i] = nums[j]
                nums[j] = a
                i += 1
                j -= 1
        return i
