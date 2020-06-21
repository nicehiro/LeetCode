from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m_p = 0
        m_t = []
        m = 0
        for i in range(len(prices)-1, -1, -1):
            m = prices[i] if prices[i] > m else m
            m_t.insert(0, m)
        for i in range(len(prices)-1):
            c = prices[i]
            m_p = m_t[i+1] - c if m_t[i+1] - c > m_p else m_p
        return m_p
