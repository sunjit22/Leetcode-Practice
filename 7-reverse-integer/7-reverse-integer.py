class Solution:
    def reverse(self, x: int) -> int:
        positive = True
        
        string_x = str(x)
        list_int = []
        for i in range(len(string_x)):
            if i == 0 and string_x[0] == "-":
                positive = False
            elif i == len(string_x)-1 and string_x[i] == "0":
                break
            elif string_x[i].isdigit():
                list_int.append(string_x[i])
                
        list_int.reverse()
        
        idx = 10**(len(list_int)-1)
        num = 0
        for i in range(len(list_int)):
            num += (int(list_int[i]) * idx)
            idx = idx/10
            
        if positive == False:
            num = num * -1

        if num > (2**31) - 1 or num < -(2**31):
            return 0            
            
        return int(num)    