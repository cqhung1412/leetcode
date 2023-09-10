from typing import List


class Solution:
    def shouldMerge(self, mergedInterval: List[int], interval: List[int]) -> bool:
        if interval[0] >= mergedInterval[0] and interval[0] <= mergedInterval[1]:
            return True
        if interval[1] >= mergedInterval[0] and interval[1] <= mergedInterval[1]:
            return True
        if interval[0] <= mergedInterval[0] and interval[1] >= mergedInterval[1]:
            return True
        return False

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted(intervals, key=lambda x: x[0])
        mergedIntervals = [sortedIntervals[0]]
        for index, interval in enumerate(sortedIntervals):
            if index == 0:
                continue
            mergedLastIndex = len(mergedIntervals) - 1
            lastMergedInterval = mergedIntervals[mergedLastIndex]
            if self.shouldMerge(lastMergedInterval, interval):
                firstValue = lastMergedInterval[0] if lastMergedInterval[0] < interval[0] else interval[0]
                lastValue = lastMergedInterval[1] if lastMergedInterval[1] > interval[1] else interval[1]
                mergedIntervals[mergedLastIndex] = [firstValue, lastValue]
            else:
                mergedIntervals.append(interval)
        return mergedIntervals


if __name__ == "__main__":
    solution = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(solution.merge(intervals=intervals))
