land = '1'
water = '0'

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nRows = len(grid)
        nCols = len(grid[0])
        
        lastRow = nRows-1
        lastCol = nCols -1
        
        
        visited = []
        for row in range(nRows):
            visited.append([False]*nCols)
        
        def dfs(i,j):
            if i>lastRow or j>lastCol or i<0 or j<0:
                return
            
            if visited[i][j]:
                return
            
            if grid[i][j] == water:
                return
            
            visited[i][j] = True

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        nIslands = 0
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == land:
                    if not visited[i][j]:
                        nIslands += 1
                        dfs(i,j)
        
        return nIslands