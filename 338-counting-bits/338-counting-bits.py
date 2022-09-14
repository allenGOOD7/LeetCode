class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        if even, add 0 in last position of binary representation
        if odd, plus 1 in last position of binary representation
        
        Base 2: 111    Base 10: 7    
        Base 2: 1110   Base 10: 14  
        Base 2: 11100  Base 10: 28 
        Base 2: 11101  Base 10: 29
        """             
        dp = [0]
        for i in range (1, n + 1):
            if i % 2 == 1:
                dp.append(dp[i-1] + 1)
            else:
                dp.append(dp[i//2])
        return dp