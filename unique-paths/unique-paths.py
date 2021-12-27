class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
#         numerator = m + n -2
#         denominator1 = min(m,n) - 1
        
#         return factorial(numerator)//(factorial(denominator1) * factorial(numerator-denominator1))

#         if m == 1 or n == 1:
#             return 1
        
#         return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        
        if (m == 0 or n == 0):
            return 0
        if (m == 1 or n == 1):
            return 1
        
        dp = [[0]*n]*m
        
        for i in range(0,m):
            dp[i][0] = 1
        
        for i in range(0,n):
            dp[0][i] = 1
        
        for i in range(1,m):
            for j in range(1, n):
                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
      
        return dp[m-1][n-1]