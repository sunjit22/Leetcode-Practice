#User function Template for python3
import sys
class Solution:
    def matrixMultiplication(self, n, p):
        # code here
        m = [[0 for x in range(n)] for x in range(n)]

        # cost is zero when multiplying one matrix.
        for i in range(1, n):
            m[i][i] = 0
    
        # L is chain length.
        for L in range(2, n):
            for i in range(1, n-L + 1):
                j = i + L-1
                m[i][j] = sys.maxsize
                for k in range(i, j):
    
                    # q = cost / scalar multiplications
                    q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
                    if q < m[i][j]:
                        m[i][j] = q
    
        return m[1][n-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends