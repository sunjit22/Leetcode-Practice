class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
#         Approach 1 : O(n)        
#         sum_ = sum(nums)
#         set_nums = set(nums)
#         sum_set = sum(set_nums) * 2
#         return sum_set - sum_

#         Approach 2 : O(log n)

        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low+high)//2
            
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            
            if nums[mid] == nums[mid+1] :
                num_left = mid-low
                if num_left % 2 == 0:
                    low = mid+2
                else:
                    high = mid-1
            elif nums[mid] == nums[mid-1]:
                num_left = (mid-1)-low
                if num_left % 2 == 0:
                    low = mid+1
                else:
                    high = mid-2
                    
        return nums[low]              
                