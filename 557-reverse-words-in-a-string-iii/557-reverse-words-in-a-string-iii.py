class Solution:
    def reverseWords(self, s: str) -> str:
#         arr = []
#         for char in s:
#             arr.append(char)
        
#         head = tail = 0
#         while tail < len(s):
#             if arr[tail] == " ":
#                 arr[head:tail] = arr[head:tail][::-1]
#                 head = tail + 1
#             tail += 1
        
#         arr[head:len(s)] = arr[head:len(s)][::-1]
        
#         return "".join(arr)
            
#         res = ""
#         head = tail = 0
#         while tail < len(s):
#             if s[tail] == " ":
#                 res += s[head:tail][::-1]
#                 res += " "
#                 head = tail + 1
#             tail += 1
        
#         res += s[head:len(s)][::-1]
#         return res
    
        res = ""
        s = s.split(" ")
        for string in s:
            res += " "
            res += string[::-1]
        return res[1:]