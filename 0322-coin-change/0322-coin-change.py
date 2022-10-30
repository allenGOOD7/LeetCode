class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(1 + dp[i - c], dp[i]) # this "1" means use coin "c"
        
        return dp[amount] if dp[amount] != amount + 1 else -1
    
        # time complexity => O(amount * len(coins))
        # space complexity => O(amount)