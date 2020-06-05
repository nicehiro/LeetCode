from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        t = []
        t.append(root)
        n = 1
        while len(t) > 0:
            p = []
            b = []
            while n > 0:
                q = t.pop(0)
                p.append(q)
                b.append(q.val)
                n -= 1
            res.append(b)
            for a in p:
                if a.left:
                    t.append(a.left)
                    n += 1
                if a.right:
                    t.append(a.right)
                    n += 1
        return res
