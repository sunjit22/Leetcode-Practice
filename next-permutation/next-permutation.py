class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Example [1,2] --> return [2,1]
        # Example [2,1] --> return [1,2]
        if(len(nums) <= 2):
            return nums.reverse()
        
        reverse_nums = sorted(nums, reverse=True)
        # If list is in reverse order, return in ascending order
        if nums == reverse_nums:
            return nums.sort()
        
        # Begin iterating backwards from second last element     
        replace_idx = len(nums)-2;  # 7
        for i in range(len(nums) - 2 , -1, -1):
            # Break when you find the element smaller than next element
            if nums[i] < nums[i+1]:
                replace_idx = i  # 4
                break; 
         
        for i in range(len(nums)-1,replace_idx, -1):
            if(nums[i] > nums[replace_idx]):
                nums[i],nums[replace_idx] = nums[replace_idx],nums[i]
                break;

        nums[replace_idx+1:] = sorted(nums[replace_idx+1:]) 
        
