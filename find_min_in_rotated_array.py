from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # self.nums = nums
        # return self.binary_search(0, len(nums))
        return self.method2(nums)

    def binary_search(self, left, right):
        if right - left == 1:
            return self.nums[left]
        if right - left == 2:
            return min(self.nums[left], self.nums[right - 1])
        if right <= left:
            return None
        mid = (left + right) // 2
        if self.nums[left] < self.nums[mid] < self.nums[right - 1]:
            return self.nums[left]
        if self.nums[left] < self.nums[mid] and self.nums[mid] > self.nums[right - 1]:
            return self.binary_search(mid, right)
        if self.nums[left] > self.nums[mid] and self.nums[mid] < self.nums[right - 1]:
            return self.binary_search(left, mid + 1)

    def method2(self, nums):
        left, right = 0, len(nums) - 1
        mid = left
        while nums[left] > nums[right]:
            if left + 1 == right:
                mid = right
                break
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
        return nums[mid]


if __name__ == "__main__":
    solu = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(solu.findMin(nums))
