class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # for i in range(32):
        #     if (n >> i) & 1 == 1:
        #         res += 1
        # return res
    
        while n:
            if n & 1 == 1:
                res += 1
            n = n >> 1
        return res