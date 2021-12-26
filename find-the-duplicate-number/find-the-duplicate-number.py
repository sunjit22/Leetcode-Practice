class Solution:
    def findDuplicate(self, nums: List[int]) -> int:        
#         Doesn't work for [2,2,2,2,2]
#         set_nums = set(nums)
#         sum_set = sum(set_nums)   
#         sum_nums = sum(nums)
#         return sum_nums - sum_set

        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]
        
        
        
        
        
        
            