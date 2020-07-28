from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        self.nums = nums
        return self.log_time()

    def linear(self):
        if len(self.nums) == 1:
            return 0
        if self.nums[0] > self.nums[1]:
            return self.nums[0]
        if self.nums[-1] > self.nums[-2]:
            return self.nums[-1]
        for i in range(1, len(self.nums)-1):
            if self.nums[i] > self.nums[i-1] and self.nums[i] > self.nums[i+1]:
                return i

    def log_time(self):
        l, r = 0, len(self.nums)-1
        while l < r:
            mid = (l + r) // 2
            if self.nums[mid] < self.nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l
