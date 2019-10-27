from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            com = target - nums[i]
            if d.get(com) != None:
                return [d.get(com), i]
            d[nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 2, 95, 4, -3], 92))
