from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        has_one = False
        for i in range(n):
            if nums[i] == 1:
                has_one = True
            nums[i] = 1 if nums[i] <= 0 or nums[i] > n else nums[i]
        if not has_one:
            return 1
        
        for num in nums:
            if abs(num) == n:
                nums[0] *= -1 if nums[0] > 0 else 1
                continue
            nums[abs(num)] *= -1 if nums[abs(num)] > 0 else 1

        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0: return n
        return n + 1


if __name__ == '__main__':
    s = Solution()
    nums = [0,-1,3,1]
    print(s.firstMissingPositive(nums))