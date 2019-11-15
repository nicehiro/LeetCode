from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                length += 1
                break
            for j in range(i+1, len(nums)):
                if nums[j] != nums[i-1]:
                    length += 1
                    nums[i] = nums[j]
                    break
        return length


if __name__ == '__main__':
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(s.removeDuplicates(nums))