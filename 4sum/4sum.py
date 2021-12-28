class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left = j+1
                right = len(nums)-1
                
                while(left < right):
                    sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_ > target :
                        right -= 1
                    elif sum_ == target:
                        res = [nums[i],nums[j],nums[left],nums[right]]
                        res.sort()
                        if res not in result:
                            result.append(res)
                        left += 1
                    else:
                        left += 1
                        
        
        result.sort()
        return result
#         def twoSum(nums, target):
#             """
#             :type nums: List[int]
#             :type target: int
#             :rtype: List[int]
#             """
#             # Create a hashmap
#             hashmap = {}
#             for i in range(len(nums)):
#                 complement = target - nums[i]
#                 if complement in hashmap:
#                     return [nums[i], complement]
#                 hashmap[nums[i]] = i;
#             return None
     
#         result = []
#         for i in range(len(nums)-2):
#             for j in range(i+1, len(nums)-1):
#                 new_arr = nums[j+1:]
#                 sum_pos = target - (nums[i] + nums[j])
#                 res_twoSum = twoSum(new_arr,sum_pos) 
#                 if res_twoSum is not None:
#                     res = [nums[i], nums[j],res_twoSum[0],res_twoSum[1]]
#                     res.sort()
#                     if res not in result:    
#                         result.append(res)
#         result.sort()            
#         return result                     
            