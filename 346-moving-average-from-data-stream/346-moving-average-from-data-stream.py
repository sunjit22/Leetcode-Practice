class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.lst = []
        

    def next(self, val: int) -> float:
        self.lst.append(val)
        
        if len(self.lst) > self.size:
            new_lst = self.lst[-self.size::]
            return sum(new_lst)/len(new_lst)
        else:
            return sum(self.lst)/len(self.lst)
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)