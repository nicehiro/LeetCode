from typing import List
import copy


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.iteration(nums)

    def recursive(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        t = self.recursive(nums[:-1])
        y = copy.deepcopy(t)
        [x.append(nums[-1]) for x in y]
        return y + t

    def iteration(self, nums: List[int]) -> List[List[int]]:
        res = [[] for _ in range(len(nums)+1)]
        res[0].append([])
        for i in range(1, len(nums)+1):
            t = copy.deepcopy(res[i-1])
            [x.append(nums[i-1]) for x in t]
            res[i] = t + res[i-1]
        return res[len(nums)]


if __name__ == '__main__':
    solu = Solution()
    nums = [1,2,3]
    print(solu.subsets(nums))
