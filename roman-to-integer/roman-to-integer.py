class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to hold values
        dict= {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000};
        
        sum = 0
        
        i = 0
        while(i < len(s)):
            if (i+1 < len(s) and (dict[s[i]] < dict[s[i+1]])):
               sum += dict[s[i+1]] - dict[s[i]]
               i += 2
 
            else:
                sum += dict[s[i]]
                i += 1
                
        return sum        
                
                    
                
            
        