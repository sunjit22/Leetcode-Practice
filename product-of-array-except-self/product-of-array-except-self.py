class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = nums[0]
        # Keep track of zero indices
        zero_index = []
        
        # Get total product of nums
        for i in range(1, len(nums)):
            # If zero exists, dont add it to product
            # Store index in zero_index 
            if nums[i] == 0:
                zero_index.append(i)
            else:
                product *= nums[i]
         
        output = []
        for i in range(len(nums)):
            # If there is no zero in nums
            if len(zero_index) == 0:
                output.append(int(product/nums[i]))
                
            # If zero exists in nums    
            else:   
                if i in zero_index:
                    # If more than one zeros exist
                    if len(zero_index) > 1:
                        output.append(0)
                    else:
                        output.append(product)
                    
                # If num is not zero, but other elements can be zero  
                elif len(zero_index) > 0:
                    output.append(0)

        return output    