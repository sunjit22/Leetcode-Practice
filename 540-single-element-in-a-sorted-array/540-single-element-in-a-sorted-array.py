class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        set_nums = set(nums)
        
        sum_set = sum(set_nums) * 2
        
        return sum_set - sum_