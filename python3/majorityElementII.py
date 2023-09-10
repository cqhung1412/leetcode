from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)
        requiredTimes = round(length / 3)
        sortedNums = sorted(nums)
        


if __name__ == "__main__":
    solution = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(solution.majorityElement(intervals=intervals))
