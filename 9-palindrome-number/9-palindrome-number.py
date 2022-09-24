class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        
        l, r = 0, len(x) - 1
        while r >= l:
            if x[r] != x[l]:
                return False
            l, r = l + 1, r - 1
        return True
        