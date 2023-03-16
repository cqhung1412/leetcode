class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for idx, x in enumerate(nums):
            try:
                nextIdx = nums.index(target-x, idx+1)
                return [idx, nextIdx]
            except ValueError:
                pass

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))