class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        start, end = 0, len(mat) - 1
        i, j = 0, len(mat[0])-1
        
        while start <= end:
            mid = (start+end)//2
            
            if mat[mid][i] == target or mat[mid][j] == target: return True
            elif mat[mid][i] < target and target < mat[mid][j]: 
                # search through mid if target is lesser than first and last element of mid
                while i <= j:
                    m = (i+j)//2
                    if mat[mid][m] == target: return True
                    elif mat[mid][m] < target:
                        i = m+1
                    elif mat[mid][m] > target:
                        j = m-1
            elif mat[mid][i] > target:
                end = mid-1
            elif mat[mid][j] < target:
                start = mid+1
        return False       