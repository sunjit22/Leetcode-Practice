class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #Data preparation
        self.columnInfo, self.rowInfo, self.matrixInfo, self.moves = self.getColumnRowInfo( board )
        self.moveAmount = len(self.moves)
        
        self.board_answer = None
        #search
        self.solveHelper(board,0)
        
        #update board
        board = self.board_answer
        
    def getColumnRowInfo( self, board: List[List[str]] ) -> Tuple["defaultdict", "defaultdict" , "defaultdict", List[int]]:
        """
            Obtains the information of what numbers are present on each column and
            on each cell and the cells that are empty to obtain the information
            of what moves needs to be done. It also obtains the information per
            submatrix of the sudoku board.        
        """
        columnInfo = defaultdict(lambda: [])
        rowInfo = defaultdict(lambda:[])
        matrixInfo = defaultdict(lambda:[])
        moves = []
        for column in range( 9 ):
            for row in range( 9 ) :
                matrixIndex = self.getMatrixIndex(row,column)
                if board[row][column] != '.':
                    number = int( board[row][column] )
                    columnInfo[ column ].append( number )
                    matrixInfo[matrixIndex].append( number )
                    
                if board[column][row] != '.':
                    rowInfo[column].append(int(board[column][row]))
                
                if board[row][column] == '.':
                    moves.append( (row,column) )
                    

        return columnInfo, rowInfo, matrixInfo, moves
        
    def checkIfValidMove( self, row:int, column:int, matrixIndex:int, number:int) -> None:
        """
            Checks if the next move is a valid one to avoid visiting it and thus save
            some time.
        """
        return self.board_answer == None and \
               number not in self.rowInfo[row] and \
               number not in self.columnInfo[column] and \
               number not in self.matrixInfo[matrixIndex]
    
    def solveHelper( self, board , index ):
        """
            Searches the solution, trying to satisfy the constraints created
            in the first part of the solveSudoku function.
            
        """
        if index == self.moveAmount:
            self.board_answer = [[num for num in row] for row in board ]
            return 
       
        row, column = self.moves[ index ]
        matrixIndex = self.getMatrixIndex(row,column)
        for number in range(1,10):
            if self.checkIfValidMove( row, column , matrixIndex, number ):
                self.solveHelperHelper( board, row, column, matrixIndex, number, index)
                
    def solveHelperHelper(self, board: List[List[int]] , row: int, column:int, matrixIndex:int, number:int, index:int) -> None:
        """
        
            updates the board and then continues searching for the valid solution
        
        """
        board[row][column] = str(number)
        self.rowInfo[row].append(number)
        self.columnInfo[column].append(number)
        self.matrixInfo[matrixIndex].append(number)
                            
        self.solveHelper(board, index + 1)
              
        self.rowInfo[row].pop(-1)
        self.columnInfo[column].pop(-1)
        self.matrixInfo[matrixIndex].pop(-1)                    

    def getMatrixIndex( self, row:int , column:int) -> int:
        """
        
        obtains the info of at what sub matrix the current cell is
        
        """
        if 0 <= row <=  2:
            if 0 <= column <= 2:
                return 0
            
            if 3 <= column <= 5:
                return 1
            
            if 6 <= column <= 8:
                return 2
            
        if 3 <= row <= 5:
            if 0 <= column <= 2:
                return 3
            
            if 3 <= column <= 5:
                return 4
            
            if 6 <= column <= 8:
                return 5
        
        if 6 <= row <= 8:
            if 0 <= column <= 2:
                return 6
            
            if 3 <= column <= 5:
                return 7
            
            if 6 <= column <= 8:
                return 8