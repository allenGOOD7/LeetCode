class Solution:
    def romanToInt(self, s:str) -> int:
        dic = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}   
        ans = 0
        for index, i in enumerate(s):
            if (index < len(s)-1) and (dic[i] < dic[s[index+1]]):
                ans -= dic[i]
            else:
                ans += dic[i]
        return ans

# testCase
s = "III"
print(Solution().romanToInt(s))
s = "IV"
print(Solution().romanToInt(s))
s = "LVIII"
print(Solution().romanToInt(s))
s = "MCMXCIV"
print(Solution().romanToInt(s))