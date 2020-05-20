from typing import List
from copy import deepcopy


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        # return self.recursive(len(nums)-1)
        return self.iteration()

    def recursive(self, i):
        if i == -1:
            return [[]]
        dp_last = self.recursive(i-1)
        t = deepcopy(dp_last)
        [x.append(self.nums[i]) for x in t]
        for x in t:
            if x not in dp_last:
                dp_last.append(x)
        if [self.nums[i]] not in dp_last:
            dp_last.append([self.nums[i]])
        return dp_last

    def iteration(self):
        dp = [[] for _ in range(len(self.nums)+1)]
        dp[0].append([])
        for i in range(1, len(self.nums)+1):
            t = deepcopy(dp[i-1])
            [x.append(self.nums[i-1]) for x in t]
            for x in dp[i-1]:
                dp[i].append(x)
            for x in t:
                if not self.is_in_list(x, dp[i]):
                    dp[i].append(x)
            if not self.is_in_list([self.nums[i-1]], dp[i]):
                dp[i].append([self.nums[i-1]])
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


if __name__ == "__main__":
    solu = Solution()
    nums = [4,4,4,1,4]
    print(solu.subsetsWithDup(nums))