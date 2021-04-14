from typing import List
from copy import deepcopy


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.nums.sort()
        res, path = [], []
        self.backtrace(nums, 0, res, path)
        return res
        # return self.recursive(len(nums)-1)
        # return self.iteration()

    def recursive(self, i):
        if i == -1:
            return [[]]
        dp_last = self.recursive(i - 1)
        t = deepcopy(dp_last)
        [x.append(self.nums[i]) for x in t]
        for x in t:
            if x not in dp_last:
                dp_last.append(x)
        if [self.nums[i]] not in dp_last:
            dp_last.append([self.nums[i]])
        return dp_last

    def iteration(self):
        dp = [[] for _ in range(len(self.nums) + 1)]
        dp[0].append([])
        for i in range(1, len(self.nums) + 1):
            t = deepcopy(dp[i - 1])
            [x.append(self.nums[i - 1]) for x in t]
            for x in dp[i - 1]:
                dp[i].append(x)
            for x in t:
                if not self.is_in_list(x, dp[i]):
                    dp[i].append(x)
            if not self.is_in_list([self.nums[i - 1]], dp[i]):
                dp[i].append([self.nums[i - 1]])
        return dp[-1]

    def is_in_list(self, x, y):
        y = deepcopy(y)
        for l in y:
            if len(x) == len(l):
                for i in x:
                    if i in l:
                        l.remove(i)
                if len(l) == 0:
                    return True
        return False

    def backtrace(self, nums: List[int], k: int, res, path):
        """
        回溯法。其实就是动态规划递归版本，也是dfs 的另一个变种。
        ref: https://leetcode-cn.com/problems/subsets-ii/solution/hui-su-fa-mo-ban-tao-lu-jian-hua-xie-fa-y4evs/"""
        res.append(deepcopy(path))
        for i in range(k, len(nums)):
            if i > k and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.backtrace(nums, i + 1, res, path)
            path.pop()


if __name__ == "__main__":
    solu = Solution()
    nums = [1, 2, 2]
    print(solu.subsetsWithDup(nums))
