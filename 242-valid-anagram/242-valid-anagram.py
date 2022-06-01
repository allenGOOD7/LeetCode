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
                
        for key, value in dic_s.items():
            if value > 0:
                return False
        
        return True