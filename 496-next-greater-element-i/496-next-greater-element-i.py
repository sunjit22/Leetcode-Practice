class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        for i in range(len(nums2)):
            hashmap[nums2[i]] = i
        
        arr = []
        for i in range(len(nums1)):
            idx = hashmap[nums1[i]]
            result = -1
            for i in range(idx+1,len(nums2)):
                if nums2[i] >= nums2[idx]:
                    result = nums2[i]
                    break
            
            arr.append(result)
                
                
        return arr        
            
            