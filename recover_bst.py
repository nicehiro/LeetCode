# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.root = root
        pass

    def recover1(self):
        nums = []
        def inorder(node: TreeNode):
            if node is None:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        def find_two_need_to_exchange():
            x = y = -1
            for i in range(len(nums)-1):
                if nums[i+1] < nums[i]:
                    y = nums[i+1]
                    if x == -1:
                        x = nums[i]
                    else:
                        break
            return x, y

        def recover(r: TreeNode, x, y, count):
            if r is not None:
                if r.val == x or r.val == y:
                    r.val = x if r.val == y else y
                    count -= 1
                if count == 0:
                    return
                recover(r.left, x, y, count)
                recover(r.right, x, y, count)

        inorder(self.root)
        x, y = find_two_need_to_exchange()
        recover(self.root, x, y, 2)
