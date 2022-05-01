class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = format(x, "b")
        y = format(y, "b")
        
        length_x = len(x)
        length_y = len(y)
        
        length = max(length_x, length_y)
        
        if length_x < length:
            difference = length - length_x
            st = "0"*difference
            x = st + x
        elif length_y < length:
            difference = length - length_y
            st = "0"*difference
            y = st + y
        
        count = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1
                
        return count        
            
            