from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        requiredTimes = len(nums) / 3
        uniqueNums = list(set(nums))
        majorityElements = []
        for num in uniqueNums:
            if nums.count(num) > requiredTimes:
                majorityElements.append(num)
        return majorityElements


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3]
    print(solution.majorityElement(nums=nums))
