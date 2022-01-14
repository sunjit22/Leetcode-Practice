class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        i = 0
        max_count = 0
        count = 0
        while i < len(nums):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                count = 0
            max_count = max(max_count, count)  
            i += 1
        return max_count    
            
                