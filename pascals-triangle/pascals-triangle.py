class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        # Build a triangle base
        for i in range(1,numRows+1):
            element = [1] * i
            arr.append(element)
            
        # Replace 1s with sum of top two elements    
        for i in range(2,numRows):
            for j in range(1,i):
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        
        return arr
        
        
        