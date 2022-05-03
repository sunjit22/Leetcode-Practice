class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                result.append(nums1[i])
        result = set(result)
        
        return list(result)        
                
        