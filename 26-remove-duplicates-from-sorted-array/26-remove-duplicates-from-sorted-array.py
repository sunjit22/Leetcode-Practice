class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_num = []
        count = 0
        
        for num in nums:
            if num not in new_num:
                new_num.append(num)
                count += 1
                
        nums[:] = new_num
        return count
        