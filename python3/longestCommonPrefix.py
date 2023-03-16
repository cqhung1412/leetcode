class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""
        strs = sorted(strs)
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return ans
            ans += strs[0][i]

        return ans
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))
    print(solution.longestCommonPrefix(["dog","racecar","car"]))