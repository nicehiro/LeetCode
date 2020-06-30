# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.nums = []
        self.find_num(root, 0)
        return sum(self.nums)

    def find_num(self, root: TreeNode, prev_num):
        if not root.left and not root.right:
            self.nums.append(prev_num * 10 + root.val)
            return
        if root.left:
            self.find_num(root.left, prev_num * 10 + root.val)
        if root.right:
            self.find_num(root.right, prev_num * 10 + root.val)
