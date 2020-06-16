# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        stack = []
        stack.append(root)
        n = 0
        while len(stack) > 0:
            for i in range(len(stack)):
                stack[i].next = stack[i+1] if i+1 < len(stack) else None
            t = 2 ** n
            for i in range(t):
                a = stack.pop(0)
                if a.left:
                    stack.append(a.left)
                if a.right:
                    stack.append(a.right)
            n += 1
        return root
