class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        if len(grid) == 1:
            return sum(grid[0])
        
        rows = len(grid)
        columns = len(grid[0])
        
        
        track = []
        for i in range(rows):
            track.append([])
            for j in range(columns):
                track[i].append(0)
        
        _sum1 = 0
        for i in range(columns):
            _sum1 += grid[0][i]
            track[0][i] = _sum1
            
        _sum2 = 0    
        for i in range(rows):
            _sum2 += grid[i][0]
            track[i][0] = _sum2 
            
        for i in range(len(track)):
            print(track[i])
            
            
        for i in range(1,rows):
            for j in range(1,columns):
                track[i][j] = min(track[i-1][j] + grid[i][j], track[i][j-1] + grid[i][j])
                
        return track[rows-1][columns-1]        
            
        
        