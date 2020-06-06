# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = []
        stack.append(root)
        t = []
        res = 0
        while len(stack) > 0:
            t += stack
            stack.clear()
            res += 1
            for n in t:
                if n.left:
                    stack.append(n.left)
                if n.right:
                    stack.append(n.right)
        t.close()
        return res
