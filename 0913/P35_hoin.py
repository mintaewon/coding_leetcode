class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[[1] for _ in range(n)] for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                grid[i+1][j+1][0] = grid[i][j+1][0] + grid[i+1][j][0]
        return grid[m-1][n-1][0]