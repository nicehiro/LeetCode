from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            if right - left == 1:
                return min(nums[left], nums[right])
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]


if __name__ == '__main__':
    solu = Solution()
    nums = [2,2,2,0,1]
    print(solu.findMin(nums))
