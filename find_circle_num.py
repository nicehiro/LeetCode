from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        not_visited = {x for x in range(n)}
        res = 0
        while not_visited:
            a = not_visited.pop()
            not_visited.add(a)
            q = [a]
            res += 1
            while q:
                p = q.pop()
                not_visited.remove(p)
                for i in range(n):
                    if i in not_visited and isConnected[p][i] == 1:
                        q.append(i)
        return res


if __name__ == '__main__':
    is_connected = [[1,1,1],[1,1,1],[1,1,1]]
    solu = Solution()
    print(solu.findCircleNum(is_connected))
