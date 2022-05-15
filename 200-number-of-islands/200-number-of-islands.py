class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        
        rows = len(grid)
        columns = len(grid[0])
        
        visited = []
        for i in range(rows):
            visited.append([False]*columns)
            
            
        def dfs(i , j , count, visited):
            if i >= rows or i < 0 or j >= columns or j < 0 or visited[i][j] == True or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            visited[i][j] = True
                
            dfs(i-1,j,count, visited)
            dfs(i+1,j,count, visited)
            dfs(i,j-1,count, visited)
            dfs(i,j+1,count, visited)
            
            
        count = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1" and visited[i][j] == False:
                    count += 1
                    dfs(i, j, count, visited)
        return count            

        
#         # Check whether grid exists
#         if grid == None or len(grid) == 0:
#             return 0
        
#         # Prereq:
#         rows = len(grid)
#         cols = len(grid[0])
#         visited = []
        
#         # Create a matrix to store track of visits
#         for row in range(rows):
#             visited.append([False]*cols)
 
#         # Dfs 
#         def dfs(i,j):
#             if i < 0 or j < 0 or i > (rows-1) or j > (cols-1) or grid[i][j] == '0' or visited[i][j]:
#                 return 
#             grid[i][j] == "0"
#             visited[i][j] = True
#             dfs(i-1, j)
#             dfs(i+1, j)
#             dfs(i, j-1)
#             dfs(i, j+1)
            
            
#         num_islands = 0
#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == "1" and not visited[i][j]:
#                     num_islands += 1
#                     dfs(i,j)
                        
#         return num_islands   
    
    
    
