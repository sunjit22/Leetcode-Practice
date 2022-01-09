class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None or len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        
        for row in range(rows):
            visited.append([False]*cols)
        
        
        
        def traverse_grid(i,j):
            if i < 0 or j < 0 or i > (rows-1) or j > (cols-1) or grid[i][j] == '0' or visited[i][j]:
                return 
            
            grid[i][j] == "0"
            visited[i][j] = True
            traverse_grid(i-1, j)
            traverse_grid(i+1, j)
            traverse_grid(i, j-1)
            traverse_grid(i, j+1)
            
            
        num_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    num_islands += 1
                    traverse_grid(i,j)
                        
        return num_islands   
    
    
    
