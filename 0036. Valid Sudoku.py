from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        big = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                current = board[i][j]
                if ((i, current) in big or 
                    (current, j) in big or 
                    ((i // 3), (j // 3), current) in big):
                    return False
                big.add((i, current))
                big.add((current, j))
                big.add((i // 3, j // 3, current))
        return True