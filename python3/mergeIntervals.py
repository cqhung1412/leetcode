from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mergedIntervals = [intervals[0]]
        for index, interval in enumerate(intervals):
            if index == 0:
                continue
            currInterval = mergedIntervals[index-1]
            if interval[0] <= currInterval[1]:
                mergedIntervals[index-1] = [currInterval[0], interval[1]]
                
        return mergedIntervals
            


if __name__ == "__main__":
    solution = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(solution.merge(intervals=intervals))
