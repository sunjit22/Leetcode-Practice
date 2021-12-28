class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        longest_length = 0
        
        for num in nums_set:
            if((num-1) not in nums_set):
                curr_length = 1
                curr_num = num
                
                while((curr_num+1) in nums_set):
                    curr_length += 1
                    curr_num += 1
                    
                longest_length = max(longest_length, curr_length)    
        return longest_length            
                
                