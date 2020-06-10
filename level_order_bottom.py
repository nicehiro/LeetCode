from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        stack = []
        stack.append(root)
        n = 1
        res = []
        while len(stack) > 0 and n > 0:
            temp = []
            a = []
            while n > 0:
                p = stack.pop(0)
                temp.append(p)
                a.append(p.val)
                n -= 1
            res.insert(0, a)
            for t in temp:
                if t.left:
                    stack.append(t.left)
                    n += 1
                if t.right:
                    stack.append(t.right)
                    n += 1
        return res
