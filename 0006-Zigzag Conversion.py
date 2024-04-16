class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        alpha = []
        for string in s:
            alpha.append(string)

        rowDiff = 2 * numRows - 2
        if rowDiff == 0:
            return s
        res = []

        for i in range(numRows):
            num = i + 1
            if num == 1 or num == numRows:    
                while num <= len(alpha):
                    res.append(alpha[num - 1])
                    num += rowDiff
                    print(num)
            else:
                while num <= len(alpha):
                    res.append(alpha[num - 1])
                    if num + rowDiff - i * 2 <= len(alpha):
                        res.append(alpha[num + rowDiff - i * 2 - 1])
                    num += rowDiff

        return "".join(res)