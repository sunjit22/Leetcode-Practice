class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # APPROACH 1
        return len(set(nums)) != len(nums)
        
        # OTHER APPROACHES
        
        # APPROACH 2
        # set_nums = set(nums)
        # return len(set_nums) < len(nums)
        
         
        # APPROACH 3    
        # set_nums = set()
        # for i in range(len(nums)):
        #     if nums[i] in set_nums:
        #         return True
        #     else:
        #         set_nums.add(nums[i])
        # return False        

        
        # APPROACH 4
        # nums.sort();
        # for i in range(0, len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True  
        # return False      