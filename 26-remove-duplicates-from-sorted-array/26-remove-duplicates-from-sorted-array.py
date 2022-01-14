class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_nums = set(nums)
        nums[:] = sorted(set_nums)
        return len(nums)
        # nums[:] = sorted(set(nums))
        # return len(nums)
        