from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        for i in range(len(nums)):
            s += nums[i] if i % 2 == 0 else 0
        return s


if __name__ == "__main__":
    nums = [6, 2, 6, 5, 1, 2]
    s = Solution()
    print(s.arrayPairSum(nums))
