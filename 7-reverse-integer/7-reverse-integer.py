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
            

        # for i in range(len(list_int)):
        #     list_int[i] = int(list_int[i])
        #     print(list_int[i])
            
        
        
        
#         int_string = str(int)
#         list_int = []
        
#         positive = True
#         for i in range(len(int_string)):
#             if i == 0 and int_string[i] == "-":
#                 positive = False
#             elif i == len(int_string) - 1 and int_string[i] == "0":
#                 break
#             elif int_string[i].isdigit():
#                 list_int.append(int_string[i])
                
        
#         list_int.reverse()
#         for i in range(len(list_int)):
#             list_int[i] = list_int[i])
#         num = "".join(list_int)
        
        # num = 10 ** (len(list_int)-1)
        # result = 1
        # for i in list_int:
        #     print(i)
        #     result = i * num + result
        #     num = num / 10
         
#         if(positive == False):
#             res = res * -1
            

        
#         return res