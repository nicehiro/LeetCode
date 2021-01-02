from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        self.prices = prices
        return self.recursive(0, k, False)

    def recursive(self, i, k, can_sell):
        if k <= 0 or i >= len(self.prices):
            return 0
        if can_sell:
            return max(self.recursive(i+1, k, True), self.recursive(i+1, k, False)+self.prices[i])
        return max(self.recursive(i+1, k-1, False), self.recursive(i+1, k, True)-self.prices[i])


if __name__ == '__main__':
    solu = Solution()
    print(solu.maxProfit(2, [3,2,6,5,0,3]))
