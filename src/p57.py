from typing import List


## Runtime 5.5%
## Memory 5.8%
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = -1, -1
        n = len(intervals)
        if n == 0:
            return [newInterval]
        for i in range(n):
            if start == -1:
                if newInterval[0] <= intervals[i][1]:
                    start = i
            if start != -1:
                if newInterval[1] >= intervals[i][0]:
                    end = i + 1
        if start == -1:
            intervals.append(newInterval)
        elif end == -1:
            intervals.insert(start, newInterval)
        else:
            overlaps = [min(newInterval[0], intervals[start][0]), max(newInterval[1], intervals[end - 1][1])]
            intervals[start:end] = [overlaps]
        return intervals