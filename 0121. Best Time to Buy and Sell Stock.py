from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return profit


# testCase
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))
prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))
prices = [7,6,4,3,1,8,2]
print(Solution().maxProfit(prices))