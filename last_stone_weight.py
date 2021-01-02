from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        return my_solu(stones)

    def best_solu(self, stones: List[int]) -> int:
        """Use priority heap.
        """
        # TODO: priority heap in python
        pass

    def my_solu(self, stones: List[int]) -> int:
        """Not the best"""
        def find_max(stones: List[int]):
            if not stones or len(stones) <= 0:
                raise Exception("stones should have elements.")
            m = -1
            m_i = -1
            for i in range(len(stones)):
                if stones[i] > m:
                    m = stones[i]
                    m_i = i
            stones.pop(m_i)
            return m
        while len(stones) > 1:
            a = find_max(stones)
            b = find_max(stones)
            if a == b:
                pass
            else:
                stones.append(abs(a - b))
        return 0 if len(stones) == 0 else stones[0]


if __name__ == '__main__':
    stones = [5, 5]
    solu = Solution()
    print(solu.lastStoneWeight(stones))
