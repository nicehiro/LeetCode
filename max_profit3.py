from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        # return max(self.recursive(0, True, 2, 0), 0)
        return self.iteration()

    def recursive(self, i, can_buy, buy_times, s):
        if i >= len(self.prices) or (can_buy and buy_times <= 0):
            return s
        if can_buy:
            return max(self.recursive(i+1, False, buy_times-1, s-self.prices[i]),
                       self.recursive(i+1, True, buy_times, s))
        return max(self.recursive(i+1, True, buy_times, s+self.prices[i]),
                   self.recursive(i+1, False, buy_times, s))

    def iteration(self):
        min_price, max_profit1, max_profit_after_buy, max_profit2 = float('inf'), 0, -float('inf'), 0
        for price in self.prices:
            min_price = min(min_price, price)
            max_profit1 = max(max_profit1, price-min_price)
            max_profit_after_buy = max(max_profit_after_buy, max_profit1-price)
            max_profit2 = max(max_profit2, max_profit_after_buy+price)
        return max_profit2


if __name__ == '__main__':
    solu = Solution()
    prices = [1,2,3,4,5]
    print(solu.maxProfit(prices))
