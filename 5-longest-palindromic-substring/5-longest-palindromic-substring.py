class Solution:
    def longestPalindrome(self, s: str) -> str:     
        if s == "" or len(s) == 0:
            return ""
        
        n=len(s)
        res=0
        
        def spread(i,j):
            while i>=0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]
        
        res=""
        for i in range(n):
            res=max(spread(i,i), spread(i,i+1),res, key=len)
        
        return res
        
#         start = 0
#         end = 0
        
#         for i in range(len(s)):
#             len1 = self.expand_around_center(s, i, i)
#             len2 = self.expand_around_center(s, i, i+1)

#             length = max(len1, len2)
#             if length > (end-start):
#                 start = i - (length-1)/2
#                 end = i + length/2
#         return s[int(start):int(end+1)]
            
#     def expand_around_center(self, s, left, right):
#         while (left >= 0 and right < len(s) and s[left] == s[right]):
#             left -= 1
#             right += 1
#         return right - left - 1          
        
#         Approach 2 : Exceeds time limit        
#         n = len(st) # get length of input string
 
#         # table[i][j] will be false if substring
#         # str[i..j] is not palindrome. Else
#         # table[i][j] will be true
#         table = [[0 for x in range(n)] for y
#                               in range(n)]

#         # All substrings of length 1 are
#         # palindromes
#         maxLength = 1
#         i = 0
#         while (i < n) :
#             table[i][i] = True
#             i = i + 1

#         # check for sub-string of length 2.
#         start = 0
#         i = 0
#         while i < n - 1 :
#             if (st[i] == st[i + 1]) :
#                 table[i][i + 1] = True
#                 start = i
#                 maxLength = 2
#             i = i + 1

#         # Check for lengths greater than 2.
#         # k is length of substring
#         k = 3
#         while k <= n :
#             # Fix the starting index
#             i = 0
#             while i < (n - k + 1) :

#                 # Get the ending index of
#                 # substring from starting
#                 # index i and length k
#                 j = i + k - 1

#                 # checking for sub-string from
#                 # ith index to jth index iff
#                 # st[i + 1] to st[(j-1)] is a
#                 # palindrome
#                 if (table[i + 1][j - 1] and
#                           st[i] == st[j]) :
#                     table[i][j] = True

#                     if (k > maxLength) :
#                         start = i
#                         maxLength = k
#                 i = i + 1
#             k = k + 1
#         res = st[start : start + maxLength]    

#         return res
        
        
        
   
            
            