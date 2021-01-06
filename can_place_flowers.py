from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        if l == 1 and flowerbed[0] == 0:
            return True if n <= 1 else False
        p = 0
        last = -2
        can = 0
        while p <= l:
            if p >= l or flowerbed[p] == 1:
                if p >= l:
                    p += 1
                if p - last >= 3:
                    can += ((p - last) - 2) // 2
                last = p
            if can >= n:
                return True
            p += 1
        return True if can >= n else False


if __name__ == '__main__':
    flowerbed = [1, 0, 0, 0, 1, 0, 0]
    n = 2
    solu = Solution()
    print(solu.canPlaceFlowers(flowerbed, n))
