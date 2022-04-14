class Solution:
  
    def isvalid(self, grid, r, c, n):
        """
        returns True: given grid is a valid sudoku board
        return False: given grid is not a valid sudoku board
        """
        for i in range(9):
            if i!=r and grid[i][c]!='.' and grid[i][c]==n:
                return False
            if i!=c and grid[r][i]!='.' and grid[r][i]==n:
                return False
            bR = 3*(r//3)+i//3
            bC = 3*(c//3)+i%3
            if bR!=r and bC!=c and grid[bR][bC]!='.' and grid[bR][bC]==n:
                return False
        return True
    
    def solveBackTrack(self, grid, t):
        for i in range(9):
            for j in range(9):
                if (i,j) in t and grid[i][j]=='.':
                    for k in t[(i,j)]:
                        if self.isvalid(grid, i, j, k):
                            grid[i][j]=k

                            if self.solveBackTrack(grid, t):
                                return True
                            else:
                                grid[i][j]='.'
                    return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        maxval = 9
        vals = ['1','2','3','4','5','6','7','8','9']
        t = {}

        safeval = True
        while safeval:
            safeval = False
            for i in range(len(board)):
                for j in range(len(board[0])):
                  #non given val
                  if board[i][j] == '.':
                    #possible vals
                    pv = []
                    #check vals
                    for k in range(0, maxval):
                        board[i][j]=vals[k]

                        if self.isvalid(board, i, j, vals[k]):
                            pv.append(vals[k])

                        board[i][j]='.'
                    #put vals in table
                    if len(pv)==1:
                        board[i][j]=pv[0]
                        safeval = True
                    else:
                        t[(i,j)]=pv
        self.solveBackTrack(board, t)    