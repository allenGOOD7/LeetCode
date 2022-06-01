class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        for digit in s:
            if digit not in dic_s:
                dic_s[digit] = 1
            else:
                dic_s[digit] += 1
        
        for digit in t:
            if digit not in dic_s or dic_s[digit] == -1:
                return False
            else:
                dic_s[digit] -= 1
                
        for key in dic_s:
            if dic_s[key] > 0:
                return False
        
        return True