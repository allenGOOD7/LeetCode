class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        for char in s:
            arr.append(char)
        
        head = tail = 0
        while tail < len(s):
            if arr[tail] == " ":
                arr[head:tail] = arr[head:tail][::-1]
                head = tail + 1
            tail += 1
        
        arr[head:len(s)] = arr[head:len(s)][::-1]
        
        return "".join(arr)
            