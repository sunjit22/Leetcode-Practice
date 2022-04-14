class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        if not any(['.' in i for i in board]): # exit condition
            return board
			
		# get all possible next moves
        moves = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    candidates = self.generate_candidates(i, j, board)
                    if not candidates:
                        return # exit if no candidates can be generated at a given position
                    moves.append((candidates, i, j))
        moves.sort(key=lambda x: len(x[0]), reverse=True)
		
		# move forward for the position with fewest candidates
        candidates, i, j = moves.pop() 
        for candidate in candidates:
            board[i][j] = candidate
            res = self.solveSudoku(board)
            if res:
                return board
            else:
                board[i][j] = '.'

    def generate_candidates(self, i, j, board): # generate candidates at a given position
        candidates = set([str(n) for n in range(1, 10)])
        for pos in range(9):
            if board[pos][j] != '.' and board[pos][j]:
                candidates.discard(board[pos][j])

            if board[i][pos] != '.':
                candidates.discard(board[i][pos])

        for ii in range(i//3 * 3, i//3*3+3):
            for jj in range(j//3 * 3, j//3*3+3):
                if board[ii][jj] != '.':
                    candidates.discard(board[ii][jj])
        return list(candidates)