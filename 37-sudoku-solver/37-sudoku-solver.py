class Solution:
    def __init__(self):
        self.assign_func = {}
        self.conflict = False
        self.dec_stack = deque() 
        self.domains = {}
       
    def allAssigned(self):
        for (i,j) in sd_spots:
            if (i,j) not in self.assign_func:
                return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #convert to string for ease of processing
        problem = ""
        for strList in board:
            for space in strList:
                problem += space

        #now perform constraint solving backtracking search
        self.domains = init_domains()
        restrict_domain(self.domains, problem)

        while True:
            self.assign_func, self.domains = self.propogate(self.domains)  #will set conflict bool if propogate cant finish

            if self.conflict == False:
                if self.allAssigned():
                    return self.solution(board) #CONVERT assignment function into the specified result format
                else:
                    clean_assign_func = copy.deepcopy(self.assign_func)
 
                    spot = self.makeDecision() #assign some value to unassigned variable
 
                     #save latest decision
                    self.dec_stack.append((copy.deepcopy(self.assign_func), spot, copy.deepcopy(self.domains), copy.deepcopy(clean_assign_func)))

            else: #CONFLICT
                self.backtrack() 
                self.conflict = False

    def propogate(self, domains):
        while True:
            for (i,j) in sd_spots:
                if len(domains[(i,j)]) == 1 and (i,j) not in self.assign_func: #Make assignment if singleton
                    self.assign_func[(i,j)] = domains[(i,j)][0]
                if (i,j) in self.assign_func and len(domains[(i,j)]) > 1: #if x has been assigned, update domain to singleton
                    domains[(i,j)] = [self.assign_func[(i,j)]]
                if len(domains[(i,j)]) == 0:
                    self.conflict = True
                    return self.assign_func, domains

            was_removed = False
            for(i, j) in sd_spots:
                if len(domains[(i, j)]) == 1:  # if singleton domain?
                    for peer in sd_peers[(i, j)]:
                        peer_domain = domains[(peer)]
                        loc_domain = domains[(i, j)]
                        for val in peer_domain:
                            if val in loc_domain:
                                was_removed = True
                                peer_domain.remove(val)

                        domains[peer] = peer_domain #update domain of the peer after removal

            if not was_removed:
                return self.assign_func, domains #time to make a decision since no more propogation possible


    def backtrack(self):
        (assign_func, x, domains, clean_assign_func) = self.dec_stack.pop()
        a = assign_func[x]
        domains[x].remove(a)

        self.assign_func = clean_assign_func
        self.domains = domains
        return

   #we want to use this heuristic:
   # ALWAYS choose the variable with the smallest domain and that is unassigned in the ass_function
   # This will effectively reduce the number of branches that could be made from this point
    def makeDecision(self):
        minDom, minVar = self.get_min_domain_and_var(self.domains)
        self.assign_func[minVar] = minDom[0] #just always choose the first element of the domain of the minVariable
        return minVar
   # we dont alter the domain until later on in propogate, we will check if this variable was assigned, and it will then alter its domain to be the single elem

   #just gets us the smallest domain variable to make a decision for
    def get_min_domain_and_var(self, domains):
        minDomLen = 42
        minDom = None
        minVar = None
        for (i, j) in sd_spots:
            if len(domains[(i,j)]) < minDomLen and (i,j) not in self.assign_func:
                minDomLen = len(domains[(i,j)])
                minDom = domains[(i,j)]
                minVar = (i,j)
        return minDom, minVar

    def solution(self, board):
        for (i,j) in sd_spots:
            board[i][j] = str(self.assign_func[(i,j)])
        return board


#######BELOW HERE IS ALL SETUP AND DEFINING DOMAINS FOR SOLVING########
########   ########   ########   ########   ########   ########   
SD_DIM = 3
SD_SIZE = SD_DIM ** 2

# domain of positions
sd_domain = list(range(0, SD_SIZE))

# domain of square assignments
sd_domain_num = list(range(1, SD_SIZE + 1))

# coordinates on sudoku board
sd_spots = [(i, j) for i in sd_domain for j in sd_domain]

sd_peers = {} 
for spot in sd_spots:
    i, j = spot

    # get row and column peers
    sd_peers[spot] = [(i,c) for c in sd_domain if c!=j] + \
                  [(r,j) for r in sd_domain if r!=i]

    # upper-left coordinate of the square unit
    ul_i = (i//SD_DIM)*SD_DIM
    ul_j = (j//SD_DIM)*SD_DIM

    # get square peers
    for rr in range(SD_DIM):
        for cr in range(SD_DIM):
            peer_spot = (ul_i+rr, ul_j+cr)
            if peer_spot != spot:
                sd_peers[spot].append(peer_spot)

# initializes domains to full possible range
def init_domains():
    domains = {}
    for i, j in sd_spots:
        domains[(i, j)] = [k for k in sd_domain_num]
    return domains

# initializes domains by applying unary constraints specified by "problem"
#if the spot is a number, reduce the domain to just that singleton value
#If the range was (1-10) or something, then it is now whatever value was in that spot on the board (like 2)
def restrict_domain(domains, problem):
    for i, j in sd_spots:
        c = problem[i*SD_SIZE+j] 
        if c != '.':
            domains[(i, j)] = [int(c)]

