from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        广度优先搜索算法。
        """
        res = []
        n = len(equations)
        for q_a, q_b in queries:
            q = [(q_a, 1)]
            visited = [False for _ in range(n)]
            if q_a == q_b:
                f = False
                for i in range(n):
                    if equations[i][0] == q_a or equations[i][1] == q_a:
                        res.append(1)
                        f = True
                        break
                if not f:
                    res.append(-1)
                continue
            while q:
                q_a, v = q.pop()
                if q_b == q_a:
                    res.append(v)
                    break
                for i in range(n):
                    if not visited[i]:
                        if equations[i][0] == q_a:
                            q.append([equations[i][1], values[i] * v])
                            visited[i] = True
                        if equations[i][1] == q_a:
                            q.append([equations[i][0], v / values[i]])
                            visited[i] = True
                if not q:
                    res.append(-1)
                    break
        return res


if __name__ == '__main__':
    equations = []
    values = []
    queries = []
    solu = Solution()
    print(solu.calcEquation(equations, values, queries))
