class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        m = len(grid)
        n = len(grid[0])
        # dfs
        def dfs(x,y):
            if x<=-1 or x>=n or y<=-1 or y>=m:
                return False
            
            if grid[y][x] == "1":
                grid[y][x] = "0"
                
                dfs(x-1,y)
                dfs(x+1,y)
                dfs(x,y-1)
                dfs(x,y+1)
                return True
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(j,i):
                    cnt += 1
        return cnt