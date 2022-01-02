class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        set_nums = set(nums)
        return len(set_nums) < len(nums)
        
         
        # set_nums = set()
        # for i in range(len(nums)):
        #     if nums[i] in set_nums:
        #         return True
        #     else:
        #         set_nums.add(nums[i])
        # return False        

                
        # nums.sort();
        # for i in range(0, len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True  
        # return False      