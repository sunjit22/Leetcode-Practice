class Solution:
     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            # Approach 1 - Not optimal
#         len_1 = len(nums1)
#         len_2 = len(nums2)
        
#         i = 0
#         j = 0
#         k = 0
#         arr = []
#         while i < len_1 and j < len_2:
#             if nums1[i] <= nums2[j]:
#                 arr.append(nums1[i])
#                 i += 1
#                 k += 1
#             else:
#                 arr.append(nums2[j])
#                 j += 1
#                 k += 1
                
#         while i < len_1:
#             arr.append(nums1[i])
#             i += 1
#             k += 1
        
#         while j < len_2:
#             arr.append(nums2[j])
#             j += 1
#             k += 1
          
#         length = len(arr)
#         if length % 2 == 0:
#             left = length//2
#             right = left+1
#             return (arr[left-1] + arr[right-1])/2
#         else:
#             mid = (length+1)//2
#             return arr[mid-1]

        # Appraoch 2 - optimal
        # New Array
        arr = nums1 + nums2
        if arr == []:
            return []
        arr.sort()
        length = len(arr)
        if length % 2 == 0:
            left = length//2
            right = left+1
            return (arr[left-1] + arr[right-1])/2
        else:
            mid = (length+1)//2
            return arr[mid-1]
            
            
            