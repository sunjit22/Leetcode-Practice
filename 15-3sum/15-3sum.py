class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        
        positive, negative, zero = [],[],[]

        for i in nums:
            if i < 0:
                negative.append(i)
            elif i > 0:
                positive.append(i)
            else:
                zero.append(i)
                
        N,P = set(negative), set(positive)        
                
        
        # Case 1 - positive, negative and zero   
        if(zero):
            for i in P:
                if -1*i in N:
                    result.add((-1*i,0,i))
                    
        # Case 2 - if i,j,k are 0 - all zeros
        if(len(zero) >= 3):
            result.add((0,0,0))             
         
        # Case 3 - 2 negatives and a positive
        for i in range(len(negative)):
            for j in range(i+1,len(negative)):
                target = -1 * (negative[i] + negative[j])
                if target in P:
                    result.add(tuple(sorted([target, negative[i], negative[j]])))
        # Case 4 - 2 positives and a negative            
        for i in range(len(positive)):
            for j in range(i+1,len(positive)):
                target = -1 * (positive[i] + positive[j])
                if target in N:
                    result.add(tuple(sorted([target, positive[i], positive[j]] )))
                    
        
          

        return result           
                    
                    
                    
                
                
                
                       