class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        # init
        row =  [0 for i in range(9)]
        column =  [0 for i in range(9)]
        grid = [0 for i in range(9)]
        empty = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = 1 << (int(board[i][j]) - 1)

                    row[i] |= num
                    column[j] |= num
                    grid[i // 3 * 3 + j // 3] |= num
                else:
                    empty[(i, j)] = 1
            
        # recursion
        def dfs():
            i, j, valid = heuristic_search()
            
            if i == -1: # full
                return True
            
            grid_index = i // 3 * 3 + j // 3
            
            for k in range(1, 10):
                num = (1 << (k - 1))
                if valid & num:
                    
                    board[i][j] = str(k)
                    row[i] |= num
                    column[j] |= num
                    grid[grid_index] |= num
                    empty.pop((i, j))
                    
                    if dfs():
                        return True
                    else:
                        board[i][j] = '.'
                        row[i] &= ~num
                        column[j] &= ~num
                        grid[grid_index] &= ~num
                        empty[(i, j)] = 1
                        
            return False

        # find best search location
        # the best location has the fewest optional numbers
        def heuristic_search():
                        
            min_count = 9
            min_valid = 0x1FF
            index_i = -1
            index_j = -1
            
            for i, j in empty.keys():
                valid =  (~row[i]) & (~column[j]) & (~grid[i // 3 * 3 + j // 3]) & 0x1FF
                
                count = 0
                for k in range(9):
                    if valid & (1 << k):
                        count += 1
                        
                if count < min_count:
                    min_count = count
                    min_valid = valid
                    index_i = i
                    index_j = j
                    
            return index_i, index_j, min_valid
            
        dfs()