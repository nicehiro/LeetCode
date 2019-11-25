from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        small, big = -1, -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                small, big = mid, mid
                while small >= 0 and nums[small] == nums[mid]:
                    small -= 1
                small += 1
                while big < len(nums) and nums[big] == nums[mid]:
                    big += 1
                big -= 1
                break
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [small, big]


if __name__ == '__main__':
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print(s.searchRange(nums, target))
