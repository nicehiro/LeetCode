from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # we need to know where this sequence is sorted.
        # if nums[mid] == nums[start], start += 1
        # if nums[mid] > nums[start], nums[start:mid] is sorted
        # if nums[mid] < nums[end], nums[mid:end] is sorted
        self.nums = nums
        self.target = target
        return self.search_iter(0, len(nums)-1)

    def search_iter(self, start, end):
        if start > end:
            return False
        mid = (start + end) // 2
        if self.nums[mid] == self.target:
            return True
        if self.nums[mid] == self.nums[start]:
            return self.search_iter(start+1, end)
        if self.nums[mid] == self.nums[end]:
            return self.search_iter(start, end-1)
        if self.nums[mid] > self.nums[start]:
            if self.nums[start] <= self.target < self.nums[mid]:
                return self.search_iter(start, mid)
            return self.search_iter(mid+1, end)
        if self.nums[mid] < self.nums[end]:
            if self.nums[mid] < self.target <= self.nums[end]:
                return self.search_iter(mid, end)
            return self.search_iter(start, mid-1)


if __name__ == '__main__':
    solu = Solution()
    # nums = [2,5,6,0,0,1,2]
    # target = 0
    nums = [3,5,1]
    target = 1
    print(solu.search(nums, target))
