from typing import List
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        m = math.floor(len(nums) / 2)
        for k, v in d.items():
            if v > m:
                return k
