class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for index, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prices[stack[-1]] -= price
                stack.pop()    
            stack.append(index)
        
        return prices