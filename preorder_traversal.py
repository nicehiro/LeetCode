from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.iteration(root)
        return self.res

    def recursive(self, root):
        if not root:
            return
        self.res.append(root.val)
        self.recursive(root.left)
        self.recursive(root.right)

    def iteration(self, root):
        stack = []
        stack.append(root)
        while len(stack) > 0:
            if stack[-1]:
                self.res.append(stack[-1].val)
                stack.append(stack[-1].left)
                continue
            stack.pop(-1)
            if len(stack) == 0:
                break
            last = stack.pop(-1)
            stack.append(last.right)
