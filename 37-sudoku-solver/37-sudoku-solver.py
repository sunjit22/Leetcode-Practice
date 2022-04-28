
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        box = lambda i,j: [(i - i%3+di, j - j%3+dj) for di in range(3) for dj in range(3)]
        neighs = lambda i,j: set([tup for k in range(9) for tup in [(k,j), (i,k)]] + box(i,j)) - {(i,j)}
        getCands = lambda i,j: set(map(str, range(1,10))) - set(board[I][J] for I,J in neighs(i,j))

        for i,j in product(range(9), range(9)):
            if board[i][j] == '.':
                for x in getCands(i,j):
                    board[i][j] = x
                    if self.solveSudoku(board): return board
                board[i][j] = '.'; return False
        return board    