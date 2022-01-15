class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = [[]]
        
        for num in nums:
            # for curr in output:
            #     output.append([curr + [num]])
            output += [curr + [num] for curr in output]
        
        result = []
        for o in output:
            if o not in result:
                result.append(o)
        return result 