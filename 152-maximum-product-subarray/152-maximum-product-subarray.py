class Solution:
   
    def maxProduct(self, nums: List[int]) -> int:
        # check the edge case of an empty array
        if not nums:
            return 0
        
        
        Mymin = Mymax = global_max = nums[0]
  
        for n in nums[1:]:
  
            temp = Mymax # retain the previous local minimum
   
           
            Mymax = max(n, n*Mymax, n*Mymin)
   
            # update local min
            Mymin = min(n, n*Mymin, n*temp)
            global_max = max(global_max, Mymax)
  
        return global_max