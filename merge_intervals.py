from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])

        k = 1
        def merge_two(i, j):
            l1, h1 = intervals[i]
            l2, h2 = intervals[j]
            if h1 < l2 or h2 < l1:
                return j + 1
            intervals.pop(j)
            intervals.pop(j-1)
            intervals.insert(j-1, [min(l1, l2), max(h1, h2)])
            return j
        
        while k < len(intervals):
            k = merge_two(k-1, k)
        return intervals


if __name__ == "__main__":
    s = Solution()
    # intervals = [[1,3],[2,6],[8,10],[15,18]]
    # intervals = [[1,4],[4,5]]
    # intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
    print(s.merge(intervals))