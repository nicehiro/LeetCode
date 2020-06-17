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
        while len(stack) > 0:
            for i in range(len(stack)):
                stack[i].next = stack[i+1] if i < len(stack)-1 else None
            t = []
            while len(stack) > 0:
                a = stack.pop(0)
                t.append(a)
            for n in t:
                if n.left:
                    stack.append(n.left)
                if n.right:
                    stack.append(n.right)
        return root
