from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.sum = sum
        self.res = []
        self.recursive(root, 0, [])
        return self.res

    def recursive(self, root: TreeNode, sum: int, t: List):
        sum = sum + root.val
        t.append(root.val)
        if not root.left and not root.right:
            if sum == self.sum:
                self.res.append(t)
            return
        if root.left:
            self.recursive(root.left, sum, t.copy())
        if root.right:
            self.recursive(root.right, sum, t.copy())
