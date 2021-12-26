class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        row_positions = set()
        col_positions = set()
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_positions.add(i)
                    col_positions.add(j)
                    
        for i in row_positions:
            for j in range(cols):
                matrix[i][j] = 0
                
                    
        for i in col_positions:
            for j in range(rows):
                matrix[j][i] = 0
                
        return matrix        
                