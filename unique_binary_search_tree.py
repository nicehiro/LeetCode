from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        self.res = []
        l = [x for x in range(1, n+1)]
        # self.recursive(l)
        # return self.res
        return self.recursive2(1, n+1)

    def recursive(self, l: List):
        if len(l) == 1:
            t = TreeNode(l[0])
            self.res.append(t)
            return [t]
        q = []
        for i in range(len(l)):
            n = TreeNode(l[i])
            t = l.copy()
            t.pop(i)
            p = self.recursive(t)
            for r in p:
                q.append(r)
                while r is not None:
                    if l[i] > r.val and r.right is None:
                        r.right = n
                        break
                    elif l[i] < r.val and r.left is None:
                        r.left = n
                        break
                    elif l[i] > r.val:
                        r = r.right
                    else:
                        r = r.left
        return q

    def recursive2(self, s, e):
        if s < e:
            return []
        if s == e:
            return [None]
        if e - s == 1:
            return [TreeNode(s)]
        res = []
        for i in range(s, e):
            left = self.recursive2(s, i)
            right = self.recursive2(i+1, e)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res


if __name__ == '__main__':
    solu = Solution()
    print(solu.generateTrees(0))

