class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        sum_set = sum(set(nums))*2
        return sum_set - sum_nums        