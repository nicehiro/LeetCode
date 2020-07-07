from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) != len(cost):
            return -1
        n = len(gas)
        for i in range(n):
            last = 0
            can_achieve = True
            for j in range(i, i+n):
                t = j % n
                last += gas[t] - cost[t]
                if last < 0:
                    can_achieve = False
                    break
            if can_achieve and j == i + n - 1:
                return i
        return -1


if __name__ == '__main__':
    solu = Solution()
    gas = []
    cost = []
    print(solu.canCompleteCircuit(gas, cost))
