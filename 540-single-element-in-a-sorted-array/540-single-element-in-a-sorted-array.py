class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        set_nums = set(nums)
        
        sum_set = 0
        for s in set_nums:
            sum_set += s
        
        sum_set = sum_set * 2
        
        return sum_set - sum_