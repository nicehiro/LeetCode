from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # divide & conque
        self.heights = heights
        # return self.DC(0, len(heights))
        return self.STACK()

    def direct(self):
        area = 0
        for i in range(len(self.heights)):
            for j in range(i, len(self.heights)):
                # find miniest height between (i, j)
                min_h = self.heights[i]
                for h in range(i, j):
                    min_h = self.heights[h] if min_h > self.heights[h] else min_h
                t = min_h * (j - i + 1)
                area = t if t > area else area
        return area

    def find_min_position(self, l, r):
        if l >= r:
            return -1
        m = self.heights[l]
        p = l
        for i in range(l, r):
            if self.heights[i] < m:
                p = i
                m = self.heights[i]
        return p

    def DC(self, l, r):
        if l >= r:
            return 0
        m_p = self.find_min_position(l, r)
        m_area = (r - l) * self.heights[m_p]
        return max(m_area, self.DC(l, m_p), self.DC(m_p+1, r))

    def STACK(self):
        l = [(-1, -1)]
        res = 0
        for i in range(len(self.heights)):
            if self.heights[i] > l[-1][1]:
                l.append((i, self.heights[i]))
            else:
                while self.heights[i] <= l[-1][1]:
                    top, height = l.pop()
                    t = height * (i - l[-1][0] - 1)
                    res = t if res < t else res
                l.append((i, self.heights[i]))
        for i in range(len(l)-1, 0, -1):
            res = max((len(self.heights) - l[i-1][0] - 1) * l[i][1], res)
        return res


if __name__ == '__main__':
    solu = Solution()
    heights = [5,4,1,2]
    print(solu.largestRectangleArea(heights))
