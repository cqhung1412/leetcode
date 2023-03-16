class Solution:
	def toCharNumDict(self, word: str) -> dict:
		charNum = {}
		for x in word:
			if x in charNum:
				charNum[x] = charNum[x] + 1
			else:
				charNum[x] = 1
		return charNum

	def isAnagram(self, s: str, t: str) -> bool:
		sCharNum = self.toCharNumDict(s)
		tCharNum = self.toCharNumDict(t)
		return sCharNum == tCharNum


if __name__ == "__main__":
	solution = Solution()
	print(solution.isAnagram("anagram", "nagaram"))
	print(solution.isAnagram("rat", "car"))
