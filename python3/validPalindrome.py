import re
class Solution:
    def cleanStr(self, s: str) -> str:
        return re.sub(r'[\W_]', '', s).lower()
    def isPalindrome(self, s: str) -> bool:
        cleaned = self.cleanStr(s)
        length = len(cleaned)
        if length == 0:
            return True
        pivot = length / 2
        for x in range(int(pivot)):
            if cleaned[x] != cleaned[length - 1 - x]:
                return False
        return True
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))  