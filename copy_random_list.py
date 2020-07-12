# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        head_copy = head
        res = Node(head.val, None, None)
        db = {}
        copy_ = res
        db[head.val] = [copy_]
        while head.next:
            n = Node(head.next.val, None, None)
            if n.val in db:
                db[n.val].append(n)
            else:
                db[n.val] = [n]
            res.next = n
            res = res.next
            head = head.next
        head = head_copy
        res = copy_
        while head:
            if head.random:
                if len(db[head.random.val]) == 1:
                    res.random = db[head.random.val][0]
                else:
                    for n in db[head.random.val]:
                        if self.check_node_equal(head.random, n):
                            res.random = n
                            break
            head = head.next
            res = res.next
        return copy_

    def check_node_equal(self, node_a, node_b):
        while node_a and node_b:
            if node_a.val != node_b.val:
                return False
            node_a = node_a.next
            node_b = node_b.next
        if (not node_a and node_b) or (not node_b and node_a):
            return False
        return True


if __name__ == '__main__':
    solu = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node1.random = node1
    node2.random = node1
    print(solu.copyRandomList(node1))
