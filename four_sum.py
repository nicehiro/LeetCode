from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        nums = sorted(nums)
        res = []
        for i in range(0, length):
            temp = nums[i]
            if (temp > target and nums[i] > 0) or (i-1 >= 0 and nums[i] == nums[i-1]):
                continue
            for j in range(i + 1, length):
                temp = nums[i] + nums[j]
                if (temp > target and nums[j] > 0) or (j-1 >= i+1 and nums[j] == nums[j-1]):
                    continue
                for k in range(j + 1, length):
                    temp = nums[i] + nums[j] + nums[k]
                    if (temp > target and nums[k] > 0) or (k-1 >= j+1 and nums[k] == nums[k-1]):
                        continue
                    left = target - temp
                    if left in nums[k+1:]:
                        res.append([nums[i], nums[j], nums[k], left])
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-3, -2, -1, 0, 0, 1, 2, 3]
    target = 0
    print(s.fourSum(nums, target))