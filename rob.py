from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.rob1(nums[0 : n - 1]), self.rob1(nums[1:n]))

    def rob1(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, 2]
    print(s.rob(nums))
