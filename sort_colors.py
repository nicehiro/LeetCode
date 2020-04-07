from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_tims = [-1 for _ in range(3)]
        i = 0
        while i < len(nums):
            n = nums[i]
            if n == 2:
                if first_tims[2] < 0:
                    first_tims[2] = i
            elif n == 1:
                if first_tims[2] >= 0 and i > first_tims[2]:
                    nums[i] = 2
                    nums[first_tims[2]] = 1
                    if first_tims[1] < 0:
                        first_tims[1] = first_tims[2]
                    first_tims[2] = first_tims[2] + 1
                elif first_tims[1] < 0:
                    first_tims[1] = i
            elif n == 0:
                p = len(nums)
                if first_tims[1] >= 0 and i > first_tims[1]:
                    p = first_tims[1]
                    x = 1
                elif first_tims[2] >= 0 and i > first_tims[2]:
                    p = first_tims[2]
                    x = 2
                elif first_tims[0] < 0:
                    first_tims[0] = i
                    i += 1
                    continue
                else:
                    i += 1
                    continue
                nums[i] = x
                nums[p] = 0
                if first_tims[0] < 0:
                    first_tims[0] = p
                first_tims[x] = first_tims[x] + 1
                if x == 1:
                    i -= 1
            i += 1


if __name__ == "__main__":
    s = Solution()
    # nums = [2,0,2,1,1,0]
    nums = [0]
    s.sortColors(nums)
    print(nums)