from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        s = []
        res = []
        s.append(root)
        n = 1
        f = 1
        while len(s) > 0:
            t = []
            while n > 0:
                a = s.pop(0)
                t.append(a)
                n -= 1
            c = []
            if f == 1:
                for d in t:
                    c.append(d)
            else:
                for d in t[::-1]:
                    c.append(d)
            res.append(c)
            f *= -1
            for b in t:
                if b.left:
                    s.append(b.left)
                    n += 1
                if b.right:
                    s.append(b.right)
                    n += 1
        return res
