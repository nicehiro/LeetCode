from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        return self.iteration(root)

    def recursive(self, root):
        if not root:
            return
        self.recursive(root.left)
        self.recursive(root.right)
        self.res.append(root.val)

    def iteration(self, root):
        stack = []
        visited = {}
        res = []
        if root:
            stack.append(root)
        while len(stack) > 0:
            left_visit = right_visit = True
            top = stack[-1]
            if top.right and top.right not in visited:
                right_visit = False
                stack.append(top.right)
            if top.left and top.left not in visited:
                left_visit = False
                stack.append(top.left)
            if left_visit and right_visit:
                res.append(top.val)
                visited[top] = True
                stack.pop(-1)
        return res

    def trick(self, root):
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
        return output[::-1]
