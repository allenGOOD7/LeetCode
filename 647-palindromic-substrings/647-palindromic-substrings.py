class Solution:
    def countSubstrings(self, s: str) -> int:
        
        
        def isPalindromic(s, l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            return res
                
        res = 0
        for i in range(len(s)):            
            res += isPalindromic(s, i, i)
            res += isPalindromic(s, i, i + 1)
        
        return res