class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#         dict = {}
        
#         for i in range(len(nums)):
#             dict[nums[i]] = dict.get(nums[i],0) + 1
#         print(dict)    
#         arr = []    
#         for key,value in dict.items():
#             arr.append([value,key])
         
#         maximum = max(arr)
#         return maximum[1]  
        # min=len(nums)/2
        # s=set(nums)
        # for num in s:
        #     if(nums.count(num)>min):
        #         return num
        
        # nums.sort()
        # return nums[len(nums)//2]
        
#         hashmap = {}        
#         for i in range(len(nums)):
#             if nums[i] in hashmap:
#                 hashmap[nums[i]] += 1
#             else:
#                 hashmap[nums[i]] = 1
        
#         nums.sort(key = lambda x:hashmap[x])
        
#         return nums[-1]
        
        
        
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
                
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate