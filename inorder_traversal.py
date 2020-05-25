# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.root = root
        self.res = []
        return self.res

    def recursive(self, node: TreeNode):
        if node is not None:
            self.recursive(node.left)
            self.res.append(node.val)
            self.recursive(node.right)

    def iteration(self):
        node = self.root
        stack = []
        while node is not None and len(stack) > 0:
            while (node is not None):
                stack.append(node)
                node = node.left
            node = stack.pop()
            self.res.append(node)
            node = node.right
