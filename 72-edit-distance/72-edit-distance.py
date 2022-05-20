class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # If one word is empty string, return length of other word
        n = len(word1)
        m = len(word2)
        
        # if one of the strings is empty
        if n * m == 0:
            return n + m
        
        # array to store the convertion history
        d = [ [0] * (m + 1) for _ in range(n + 1)]
        
        # init boundaries
        for i in range(n + 1):
            d[i][0] = i
        for j in range(m + 1):
            d[0][j] = j
        
        # DP compute 
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = d[i - 1][j] + 1
                down = d[i][j - 1] + 1
                left_down = d[i - 1][j - 1] 
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                d[i][j] = min(left, down, left_down)
        
        return d[n][m]
        
#         if len(word1) == 0:
#             return len(word2)
#         elif len(word2) == 0:
#             return len(word1)
        
#         n = len(word1)
#         m = len(word2)
        
        
#         grid = []
        
#         for i in range(n+1):
#             grid.append([])
#             for j in range(m+1):
#                 grid[i].append(0)
                
#         for i in range(n):
#             grid[i][0] = i
            
#         for j in range(m):
#             grid[0][j] = j
            
#         for i in range(1, n+1):
#             for j in range(1, m+1):
#                 left = grid[i-1][j] + 1
#                 down = grid[i][j-1] + 1
#                 left_down = grid[i-1][j-1]
#                 if word1[i - 1] != word2[j - 1]:
#                     left_down += 1
#                 grid[i][j] = min(left,down,left_down)
                
#         return grid[n][m]
                
                
        