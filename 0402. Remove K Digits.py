class Solution:
    def removeKDigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while k > 0 and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        res = ''.join(stack)
        return str(int(res)) if res else "0"

# testCase
num = "1432219"
k = 3
print(Solution().removeKDigits(num, k))
num = "10200"
k = 1
print(Solution().removeKDigits(num, k))
num = "10"
k = 2
print(Solution().removeKDigits(num, k))