from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return self.XOR(nums)

    def normal(self, nums):
        res = {}
        for n in nums:
            if res.get(n):
                res.pop(n)
            else:
                res[n] = 1
        return [*res][0]

    def XOR(self, nums):
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    solu = Solution()
    nums = [4,1,2,1,2]
    print(solu.singleNumber(nums))