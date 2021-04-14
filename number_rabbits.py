from typing import List
import math


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        nums = {}
        for ans in answers:
            if (ans + 1) not in nums:
                nums[ans + 1] = 1
            else:
                nums[ans + 1] += 1
        res = 0
        for k, v in nums.items():
            res += k * (math.ceil(v / k))
        return res
