class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        
        return x == x[-1::-1]
        