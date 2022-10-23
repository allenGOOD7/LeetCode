class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        fresh = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1
        
        rows = len(grid)
        cols = len(grid[0])
        times = 0
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for hor, ver in direction:
                    row, col = r + hor, c + ver
                    if row < 0 or row == rows or col < 0 or col == cols or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            times += 1
        return times if fresh == 0 else -1