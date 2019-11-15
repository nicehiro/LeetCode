from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i-1]:
                temp = nums[i-1]
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > temp:
                        nums[i-1] = nums[j]
                        nums[j] = temp
                        self.reverse(nums, i, len(nums)-1)
                        break
                break
            i -= 1
        if i == 0:
            self.reverse(nums, 0, len(nums)-1)

    def reverse(self, nums, s, e):
        while s < e:
            temp = nums[s]
            nums[s] = nums[e]
            nums[e] = temp
            s += 1
            e -= 1


if __name__ == '__main__':
    s = Solution()
    nums = [3,2,1]
    s.nextPermutation(nums)
    print(nums)