from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_max = max_sofar = nums[0]
        for i in nums[1:]:
            curr_max = max(i, i + curr_max)
            max_sofar = max(max_sofar, curr_max)
        return max_sofar


if __name__ == '__main__':
    s = Solution()
    nums = [-1]
    print(s.maxSubArray(nums))
