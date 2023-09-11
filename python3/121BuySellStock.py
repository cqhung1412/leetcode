from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		print(prices)
		sortedPrices = sorted(prices)
		minPrice = sortedPrices[0]
		maxPrice = sortedPrices[-1]
		minIndex = prices.index(minPrice)
		maxIndex = prices.index(maxPrice)
		if maxIndex < minIndex:
			prices.remove(maxPrice if maxIndex == 0 else minPrice)
			return self.maxProfit(prices=prices)
		else:
			return maxPrice - minPrice
		


if __name__ == "__main__":
	solution = Solution()
	# prices = [7,1,5,3,6,4]
	prices = [2,1,2,1,0,1,2]
	print(solution.maxProfit(prices=prices))
