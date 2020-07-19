from typing import List


class Node:
    def __init__(self, value: None):
        self.value = value
        self.left = None
        self.right = None


def preorder_recursive(root: Node):
    if not root:
        return
    print(root.value)
    if root.left:
        preorder_recursive(root.left)
    if root.right:
        preorder_recursive(root.right)


def preorder_iteration(root: Node):
    stack = []
    stack.append(root)
    visited = {}
    while len(stack) > 0:
        top = stack[-1]
        if top not in visited:
            visited[top] = True
            print(top.value)
        if top.left and top.left not in visited:
            stack.append(top.left)
        elif top.right and top.right not in visited:
            stack.append(top.right)
        else:
            stack.pop(-1)


def inorder_recursive(root: Node):
    if not root:
        return
    if root.left:
        inorder_recursive(root.left)
    print(root.value)
    if root.right:
        inorder_recursive(root.right)


def inorder_iteration(root: Node):
    if not root:
        return None
    stack = []
    visited = {}
    stack.append(root)
    while len(stack) > 0:
        top = stack[-1]
        if top.left and top.left not in visited:
            stack.append(top.left)
            continue
        if top in visited:
            stack.pop(-1)
            continue
        print(top.value)
        visited[top] = True
        if top.right and top.right not in visited:
            stack.append(top.right)


def postorder_recursive(root: Node):
    if not root:
        return
    if root.left:
        postorder_recursive(root.left)
    if root.right:
        postorder_recursive(root.right)
    print(root.value)


def postorder_iteration(root: Node):
    stack = []
    visited = {}
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
            print(top.value)
            stack.pop(-1)
            visited[top] = True


def construct_binary_tree(node_list: List[Node]):
    """Use LeetCode build tree method.
    """
    if not node_list or len(node_list) == 0:
        return None
    nodes = [Node(i) if i != None else None for i in node_list]
    i = 0
    for node in nodes:
        if not node:
            continue
        node.left = nodes[i+1]
        node.right = nodes[i+2]
        i += 2
    return nodes[0]


if __name__ == '__main__':
    nodes = [1, 2, 3, None, None, 4, None, None, 5, None, None]
    root = construct_binary_tree(nodes)
    postorder_iteration(root)
