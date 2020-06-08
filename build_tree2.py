from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0 or len(postorder) == 0 or len(inorder) != len(postorder):
            return None
        self.inorder = inorder
        self.postorder = postorder
        self.hash_inorder = self.__hash_inorder()
        return self.recursive(0, len(self.inorder), len(self.inorder)-1)

    def __hash_inorder(self):
        return {self.inorder[i]: i for i in range(len(self.inorder))}

    def recursive(self, i, j, k):
        if i >= j or k < 0:
            return None
        val = self.postorder[k]
        pos = self.hash_inorder[val]
        root = TreeNode(val)
        root.left = self.recursive(i, pos, k-j+pos)
        root.right = self.recursive(pos+1, j, k-1)
        return root
