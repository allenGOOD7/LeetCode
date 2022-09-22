class Solution:
    def reverseWords(self, s: str) -> str:            
        s += " "
        res = ""
        head = tail = 0
        while tail < len(s):
            if s[tail] == " ":
                res += s[head:tail][::-1]
                res += " "
                head = tail + 1
            tail += 1
        
        return res[:-1]
    
        # res = ""
        # s = s.split(" ")
        # for string in s:
        #     res += " "
        #     res += string[::-1]
        # return res[1:]