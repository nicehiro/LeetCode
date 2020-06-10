from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        self.nums = nums
        return self.recursive(0, len(nums))

    def recursive(self, s, e):
        if s >= e:
            return None
        m = (s + e) // 2
        root = TreeNode(self.nums[m])
        root.left = self.recursive(s, m)
        root.right = self.recursive(m+1, e)
        return root
