class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        
        nums.sort(key=lambda x: (hashmap[x], -x))
        return nums   
        