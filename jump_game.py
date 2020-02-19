from typing import List
from functools import reduce


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # return self.jump_recursive(nums, 0)
        # return self.jump_iteration(nums)
        return self.jump_greedy(nums)

    def jump_recursive(self, nums, i):
        if i >= len(nums):
            return False
        if i == len(nums)-1:
            return True
        if nums[i] == 0:
            return False
        res = [self.jump_recursive(nums, i+x) for x in range(1, nums[i]+1)]
        return reduce(lambda x, y: x or y, res)

    def jump_iteration(self, nums):
        dp = [False] * len(nums)
        n = len(nums) - 1
        dp[n] = True
        for i in range(n-1, -1, -1):
            if nums[i] == 0:
                continue
            for j in range(1, nums[i]+1):
                if i + j > n:
                    break
                if dp[i+j]:
                    dp[i] = True 
                    break
        return dp[0]

    def jump_greedy(self, nums):
        last_pos = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0


if __name__ == "__main__":
    s = Solution()
    # nums = [2,3,1,1,4]
    nums = [3,2,1,0,4]
    # nums = [2,0,0]
    print(s.canJump(nums))