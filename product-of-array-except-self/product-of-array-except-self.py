class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = nums[0]
        zero_index = []
        for i in range(1, len(nums)):
            if nums[i] == 0:
                zero_index.append(i)
            else:
                product *= nums[i]
         
        output = []
        for i in range(len(nums)):
            if len(zero_index) == 0:
                output.append(int(product/nums[i]))
            else:     
                if i in zero_index and len(zero_index) > 1:
                    output.append(0)
                elif i in zero_index: 
                    output.append(product)
                elif i not in zero_index and len(zero_index) > 0:
                    output.append(0)

        return output    