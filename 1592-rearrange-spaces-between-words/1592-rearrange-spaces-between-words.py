class Solution:
    def reorderSpaces(self, text: str) -> str:
        words_list = text.split()
        num_spaces = text.count(' ')
        num_words = len(words_list)
        
        if num_words == 1:
            return(words_list[0] + ' ' * num_spaces)
        else:
            q, r = divmod(num_spaces, num_words - 1)
            return( (' ' * q).join(words_list) + ' ' * r )

    
    
    
    
        # Approach 2
#         words = text.split()
#         num_words=len(words)
        
#         count = 0
#         for i in range(len(text)):
#             if text[i] == " ":
#                 count += 1
                
#         if num_words == 1:
#             result = words[0] 
#             for i in range(count):
#                 result += " "
#             return result    
                
#         formula = int(count/(num_words-1))
        
#         result = ""
#         for i in range(num_words):
#             result += words[i]
#             if i != num_words-1:
#                 for j in range(formula):
#                     result += " " 
#                 count -= formula
                
            
#         if count > 0:
#             for i in range(count):
#                 result += " "
#         return result    
        
        
        
        
        