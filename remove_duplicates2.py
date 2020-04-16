from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t = 0
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                t += 1
            else:
                t = 0
            if t >= 2:
                nums.pop(i)
                t -= 1
            else:
                i += 1
        return len(nums)


if __name__ == "__main__":
    solu = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    print(solu.removeDuplicates(nums))