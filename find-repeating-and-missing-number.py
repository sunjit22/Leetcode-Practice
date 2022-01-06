class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        A1=set(A)
        A1=list(A1)
        a=sum(A)-sum(A1)
        n=len(A)
        b=int(a-sum(A)+(n*(n+1)/2))
        # print(a,b)
        return(a,b)
