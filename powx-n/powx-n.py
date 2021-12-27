class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n ==0:
                return 1
            if n == 1:
                return x
            
            half = power(x, n//2)
            
            if (n%2 == 0):
                return half * half 
            else:
                return half * half * x
            
        if(n<0):
            return 1/(power(x,abs(n)))
        else: 
            return power(x,n)
    