class Solution:
	def reverseString(self, s: list[str]) -> None:
		"""
		Do not return anything, modify s in-place instead.
		"""
		length = len(s)
		pivot = length / 2
		for x in range(int(pivot)):
			s[x], s[length - 1 - x] = s[length - 1 - x], s[x] 


if __name__ == "__main__":
	solution = Solution()
	array = ["h", "e", "l", "l", "o"]
	solution.reverseString(array)
	print(array)
	array = ["H", "a", "n", "n", "a", "h"]
	solution.reverseString(array)
	print(array)