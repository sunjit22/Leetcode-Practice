class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        result = ""
        array = list(s)
        sign = +1
        if(len(array) == 0):
            return 0
        if(array[0] == "-"):
            sign = -1 
        
        if (array[0] == "-" or array[0] == "+"):
            del array[0]
                
        
        i = 0 
        result = 0
        while(i < len(array) and array[i].isdigit()):
            result = result * 10 + int(array[i]) #ord(array[i]) - ord('0')
            i += 1
              
        result = result * sign  
        

        if(result < pow(-2,31)):
            result = pow(-2,31) 
        if(result >= pow(2,31)):
            result = pow(2,31) - 1
        return result
        