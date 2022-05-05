class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s = list(s)
        t = list(t)
        
        len1 = len(s)
        len2 = len(t)
        if len1 == len2:
            return ""
        elif len1 > len2:
            for i in range(len(s)):
                if s[i] in t:
                    t[t.index(s[i])] = "0"
                else:    
                    return s[i]
        else:
            for i in range(len(t)):
                if t[i] in s:
                    s[s.index(t[i])] = "0"
                else:
                    return t[i]
            
       
        