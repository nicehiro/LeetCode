from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return self.greedy_insert(intervals, newInterval)

    def normal_insert(self, intervals, newInterval):
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        if intervals[0][0] > newInterval[0]:
            intervals.insert(0, newInterval)
        res = [intervals[0]]
        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[0] and (i+1 >= len(intervals) or intervals[i+1][0] > newInterval[0]):
                intervals.insert(i+1, newInterval)
        for i in range(1, len(intervals)):
            a = res[-1]
            b = intervals[i]
            if a[1] >= b[0]:
                res[-1] = [min(a[0], b[0]), max(a[1], b[1])]
            else:
                res.append(b)
        return res

    def greedy_insert(self, intervals, new_interval):
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        res = []
        i = 0
        while i < len(intervals):
            if intervals[i][0] < new_interval[0] and intervals[i][1] < new_interval[0]:
                res.append(intervals[i])
                i += 1
            else:
                break
        if i >= len(intervals) or intervals[i][0] < new_interval[0]:
            intervals.insert(i+1, new_interval)
        else:
            intervals.insert(i, new_interval)
        temp = intervals[i]
        j = i + 1
        while j < len(intervals):
            if temp[1] < intervals[j][0]:
                break
            temp = [min(temp[0], intervals[j][0]), max(temp[1], intervals[j][1])]
            j += 1
        res.append(temp)
        for k in range(j, len(intervals)):
            res.append(intervals[k])
        return res
        

if __name__ == "__main__":
    s = Solution()
    intervals = [[1,5]]
    newInterval = [2,8]
    print(s.insert(intervals, newInterval))