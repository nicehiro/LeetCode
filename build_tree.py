from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0 or len(preorder) != len(inorder):
            return None
        self.preorder = preorder
        self.inorder = inorder
        self.hash_order = self.hash_inorder()
        return self.recursive(0, len(self.preorder), 0)

    def hash_inorder(self):
        return {self.inorder[i]: i for i in range(len(self.inorder))}

    def recursive(self, i, j, k):
        if i >= j:
            return None
        if k >= len(self.preorder):
            return None
        v = self.preorder[k]
        root = TreeNode(v)
        pos = self.hash_order[v]
        root.left = self.recursive(i, pos, k+1)
        root.right = self.recursive(pos+1, j, k+pos-i+1)
        return root


if __name__ == '__main__':
    solu = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9, 3, 15, 20, 7]
    solu.buildTree(preorder, inorder)
