class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for digit in magazine:
            if digit not in dic:
                dic[digit] = 1
            else:
                dic[digit] += 1
                
        for digit in ransomNote:
            if digit not in dic or dic[digit] - 1 < 0:
                return False
            dic[digit] -= 1
            
        return True