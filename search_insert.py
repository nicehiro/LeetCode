from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if nums[mid] < target:
            return mid + 1
        return mid


if __name__ == '__main__':
    s = Solution()
    nums = [1,3,5,6]
    target = 7
    print(s.searchInsert(nums, target))