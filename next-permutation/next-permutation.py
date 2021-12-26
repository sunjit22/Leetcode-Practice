class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums) <= 2):
            return nums.reverse()
        
        reverse_nums = sorted(nums, reverse=True)
        if nums == reverse_nums:
            return nums.sort()
            
        replace_idx = len(nums)-2;
        for i in range(len(nums) - 2 , -1, -1):
            if nums[i] < nums[i+1]:
                replace_idx = i 
                break;
         
        for i in range(len(nums)-1,replace_idx, -1):
            if(nums[i] > nums[replace_idx]):
                nums[i],nums[replace_idx] = nums[replace_idx],nums[i]
                break;

        nums[replace_idx+1:] = sorted(nums[replace_idx+1:]) 
        
