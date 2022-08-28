class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        dic = {}
        
        row = len(mat)
        col = len(mat[0])
        
        for i in range(row):
            for j in range(col):
                if i - j not in dic:
                    dic[i-j] = [mat[i][j]]
                else:
                    dic[i-j].append(mat[i][j])
        
        for key in dic.keys():
            dic[key].sort(reverse=True)
        
        for i in range(row):
            for j in range(col):
                mat[i][j] = dic[i-j].pop()
        
        return mat