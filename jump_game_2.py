from typing import List


class Solution:
    def __init__(self):
        self.max_int = 9999999

    def jump(self, nums: List[int]) -> int:
        # return self.recursive(0, nums)
        # return self.iteration(nums)
        return self.greedy(nums)

    def recursive(self, i, nums):
        """Recursive method.
        """
        if i == len(nums)-1:
            return 0
        if i >= len(nums):
            return self.max_int
        a = [1 + self.recursive(i+x, nums) for x in range(1, nums[i]+1)]
        return min(a)

    def iteration(self, nums):
        """Iteration method.
        """
        if len(nums) == 1:
            return 0
        res = [0] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            j = i + 1
            tmp = []
            while j < min(len(nums), i + nums[i] + 1):
                tmp.append(1 + res[j])
                j += 1
            if len(tmp) == 0:
                res[i] = self.max_int
            else:
                res[i] = min(tmp)
        return res[0]
        
    def greedy(self, nums):
        """Greedy method.
        """
        if len(nums) == 1:
            return 0
        i = 0
        res = 0
        while i < len(nums):
            start = i + 1
            end = i + nums[i]
            max_j = -1
            res += 1
            j = i + 1
            while j < min(end + 1, len(nums)):
                if j == len(nums) - 1:
                    return res
                if nums[j] + j > max_j:
                    max_j = nums[j] + j
                    i = j
                j += 1
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [4,1,1,3,1,1,1]
    print(s.jump(nums))
