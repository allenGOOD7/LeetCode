class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            dp = [0] * (n + 1)
            dp[0] = 0
            dp[1] = 1
            for i in range(2, n + 1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[-1]