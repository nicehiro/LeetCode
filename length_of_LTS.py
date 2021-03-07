from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.method2(nums)

    def method2(self, nums):
        """动态规划"""
        dp = [1]
        l = len(nums)
        for i in range(1, l):
            res = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    res = max(res, 1 + dp[j])
            dp.append(res)
        return max(dp)

    def method1(self, nums):
        """单调子序列 + 动态规划      超时 =。="""
        l = len(nums)
        dp = [[]]
        for i in range(l):
            for s in dp.copy():
                if s and nums[i] <= s[-1]:
                    t = s.copy()
                    while t and nums[i] <= t[-1]:
                        t.pop(-1)
                    t.append(nums[i])
                    dp.append(t)
                else:
                    s.append(nums[i])
        res = 0
        for d in dp:
            res = max(res, len(d))
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 0, 3, 2, 3]
    # nums = [7, 7, 7, 7]
    print(s.lengthOfLIS(nums))
