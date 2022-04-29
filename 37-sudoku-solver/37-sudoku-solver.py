'''
The wrapped sudoku board.

Instead of row+column indices, we use a single number (0-81) as  
reference to the cells. Such a reference is called `ref`.
'''
class Board:
    def __init__(self, board):
        self._board = board
        
    def get(self, ref): # wrapped getter
        i, j = divmod(ref, 9)
        char = self._board[i][j]
        return None if char == "." else int(char)
    
    def put(self, ref, num): # wrapped setter
        i, j = divmod(ref, 9)
        char = "." if num is None else str(num)
        self._board[i][j] = char
        
    def row_refs(self, i): # return refs of cells in the i-th row
        return [i*9+j for j in range(9)]
    
    def col_refs(self, j): # return refs of cells in the j-th column
        return [i*9+j for i in range(9)]
    
    def box_refs(self, k): # return refs of cells in the k-th box
        r, c = divmod(k, 3)
        base = r*27 + c*3
        return [base + x for x in (0,1,2, 9,10,11, 18,19,20)]
    
    def get_ijk(self, ref): # return which row, col, box the `ref` is at
        i, j = divmod(ref, 9)
        k = (i//3) * 3 + (j//3)
        return i, j, k
    
    def is_valid_at(self, ref): # check validity at `ref`
        i, j, k = self.get_ijk(ref)
        for refs in self.row_refs(i), self.col_refs(j), self.box_refs(k):
            nums = list(filter(lambda x: x, map(self.get, refs)))
            if len(set(nums)) < len(nums):
                return False
        return True

class Solution:    
    '''
    1. very naive DFS solution. Just try the cells left to right, top to bottom,
       testing every number from 1 to 9.
    ''' 
    def naive(self, board: List[List[str]]) -> None:
        b = Board(board)
        blanks = [i for i in range(81) if b.get(i) is None]
        digits = range(1, 10) # from 1 to 9
        
        def solve(blank_index):
            if blank_index == len(blanks): # we have solved it!
                return True
            blank = blanks[blank_index]
            for num in digits:
                b.put(blank, num) # try filling in a number
                if b.is_valid_at(blank) and solve(blank_index + 1):
                    return True
            b.put(blank, None) # revert changes
            return False
        assert solve(0), "It is guaranteed that the input board has only one solution."
        
    '''
    2. we introduce a few improvements:
      a) we pre-compute the choices set for each cell, before the DFS process.
      b) we firstly fill the blanks with the least choices.
    '''
    def less_naive(self, board: List[List[str]]) -> None:
        b = Board(board)
        blanks = [i for i in range(81) if b.get(i) is None]
        digits = range(1, 10) # from 1 to 9
        
        blank_to_choices = {blank:set() for blank in blanks}
        for blank, choices in blank_to_choices.items():
            for num in digits:
                b.put(blank, num)
                if b.is_valid_at(blank):
                    choices.add(num)
            b.put(blank, None)
            
        blanks.sort(key = lambda blank: len(blank_to_choices[blank]))
        
        def solve(blank_index):
            if blank_index == len(blanks):
                return True
            blank = blanks[blank_index]
            for num in blank_to_choices[blank]:
                b.put(blank, num)
                if b.is_valid_at(blank) and solve(blank_index + 1):
                    return True
            b.put(blank, None)
            return False
        assert solve(0), "It is guaranteed that the input board has only one solution."
        
    '''
    3. we introduce some more improvements:
      a) we update the choices dynamically, changing it in each step.
      b) we keep track of the lengths of the choice sets, and always pick the blank
         with the least choices at each step.
      c) we will not use b.is_valid_at; instead, a dead end is identified when some
         choice set turns empty.
    '''
    def improved(self, board: List[List[str]]) -> None:
        b = Board(board)
        blanks = set(i for i in range(81) if b.get(i) is None) # use set instead
        digits = range(1, 10) # from 1 to 9
        
        ## for each cell, pre-compute a set of blanks (a.k.a. `friends`) that is in
        ##  the same row, column or box:
        friends = [set() for i in range(81)]
        for me in range(81):
            i, j, k = b.get_ijk(me)
            for refs in b.row_refs(i), b.col_refs(j), b.box_refs(k):
                for ref in refs:
                    if ref in blanks:
                        friends[me].add(ref)
        
        blank_to_choices = {blank:set(digits) for blank in blanks} # start from all-nine
        
        ## keeps track of the choice counts of each blank, shall be useful later
        count_to_blanks = [set() for i in range(10)]
        count_to_blanks[9] = set(x for x in blanks)
        
        # helper function (closure) to atomically remove a choice from a `blank`.
        # returns True iff really removed.
        def remove_choice(blank, num):
            choices = blank_to_choices[blank]
            if num in choices:
                count_to_blanks[len(choices)].remove(blank)
                choices.remove(num)
                count_to_blanks[len(choices)].add(blank)
                return True
            return False
        # helper function (closure) to atomically revert the change of `remove_choice`.
        # exists only for DFS's sake.
        def add_choice(blank, num):
            choices = blank_to_choices[blank]
            count_to_blanks[len(choices)].remove(blank)
            choices.add(num)
            count_to_blanks[len(choices)].add(blank)
        
        ## update the choices sets using the initial state:
        for me in range(81):
            num = b.get(me)
            if num is None: # a blank
                continue
            for friend in friends[me]:
                remove_choice(friend, num)
                
        ## okay, finally we can write our DFS:
        def solve():
            if len(blanks) == 0: # solved!
                return True
            if len(count_to_blanks[0]) > 0: # dead end!
                return False
            for i in range(1, 10): # pick the blank with least choice
                if len(count_to_blanks[i]) > 0:
                    me = count_to_blanks[i].pop() # pop, because it will be filled soon
                    blanks.remove(me)
                    break
            choices = blank_to_choices[me]
            for num in choices:
                b.put(me, num)
                updated_friends = [] # record this in order to revert later
                for friend in friends[me]:
                    if friend not in blanks: # has been filled
                        continue
                    if remove_choice(friend, num):
                        updated_friends.append(friend)
                if solve():
                    return True
                # alright, now let's do the revert jobs. first, revert in-loop changes:
                b.put(me, None) 
                for friend in updated_friends:
                    add_choice(friend, num)
            # then, revert out-of-loop changes:
            count_to_blanks[len(choices)].add(me)
            blanks.add(me)
            return False # dead end!
        
        assert solve(), "It is guaranteed that the input board has only one solution."
        
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # self.naive(board) -- Time Limit Exceeded (416ms on the default testcase)
        # self.less_naive(board) -- Accepted, 1760ms (68ms on the default testcase)
        self.improved(board) # -- Accepted, 40ms