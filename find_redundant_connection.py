from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        return self.simple(edges)

    def stupid(self, edges):
        if not edges:
            return []
        sets = [set([i + 1]) for i in range(len(edges))]
        res = []
        for edge in edges:
            a, b = edge
            a_i = b_i = -1
            for i, s in enumerate(sets):
                if a in s:
                    a_i = i
                if b in s:
                    b_i = i
            if a_i == b_i:
                return edge
            a_s = sets[a_i]
            b_s = sets[b_i]
            sets.remove(a_s)
            sets.remove(b_s)
            sets.append(set.union(a_s, b_s))

    def simple(self, edges):
        parent = list(range(len(edges) + 1))

        def find_parent(node):
            nonlocal parent
            if parent[node] != node:
                parent = find_parent(parent[node])

        def union(node_a, node_b):
            parent[find_parent[node_a]] = parent[node_b]

        for a, b in edges:
            if find_parent(a) != find_parent(b):
                union(a, b)
            else:
                return [a, b]
        return []


if __name__ == "__main__":
    edges = [
        [9, 10],
        [5, 8],
        [2, 6],
        [1, 5],
        [3, 8],
        [4, 9],
        [8, 10],
        [4, 10],
        [6, 8],
        [7, 9],
    ]
    solu = Solution()
    print(solu.findRedundantConnection(edges))