from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 2:
            return 1
        existedNums = [None]*length
        for num in nums:
            if existedNums[num-1] == num:
                return num
            existedNums[num-1] = num


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 4, 2, 2]
    print(solution.findDuplicate(nums=nums))
