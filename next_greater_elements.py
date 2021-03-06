from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        l = len(nums)
        res = [-1 for _ in range(l)]
        for i in range(2 * l):
            while stack and nums[i % l] > nums[stack[-1]]:
                a = stack.pop(-1)
                res[a] = nums[i % l]
            stack.append(i % l)
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 3]
    print(s.nextGreaterElements(nums))
