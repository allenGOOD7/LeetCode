class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        head = tail = -1
        
        s = " " + s + " "
        for i in range(len(s) - 2, 0, -1):
            if s[i + 1] == " " and s[i] != " ":
                tail = i
            if s[i - 1] == " " and s[i] != " ":
                head = i
                res += s[head:tail+1]
                res += " "

        return res[:-1]