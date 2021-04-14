from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self.method2(nums)

    def method1(self, nums):
        t = 0
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                t += 1
            else:
                t = 0
            if t >= 2:
                nums.pop(i)
                t -= 1
            else:
                i += 1
        return len(nums)

    def method2(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return len(nums)
        slow, fast = 2, 2
        while fast < n:
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == "__main__":
    solu = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    print(solu.removeDuplicates(nums))
