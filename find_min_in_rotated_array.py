from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        self.nums = nums
        return self.binary_search(0, len(nums))

    def binary_search(self, left, right):
        if right - left == 1:
            return self.nums[left]
        if right - left == 2:
            return min(self.nums[left], self.nums[right-1])
        if right <= left:
            return None
        mid = (left + right) // 2
        if self.nums[left] < self.nums[mid] < self.nums[right-1]:
            return self.nums[left]
        if self.nums[left] < self.nums[mid] and self.nums[mid] > self.nums[right-1]:
            return self.binary_search(mid, right)
        if self.nums[left] > self.nums[mid] and self.nums[mid] < self.nums[right-1]:
            return self.binary_search(left, mid+1)


if __name__ == '__main__':
    solu = Solution()
    nums = [4,5,6,7,0,1,2]
    print(solu.findMin(nums))
