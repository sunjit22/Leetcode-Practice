class Solution:
     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        len_x = len(nums1)
        len_y = len(nums2)
        low_val = 0
        high_val = len_x

        while(low_val <= high_val):
            x_mid = int((low_val + high_val)/2)
            y_sep = int((len_x+len_y+1)/2 - x_mid)
            if x_mid == 0:
                x_left_max = -math.inf
            else:
                x_left_max = nums1[x_mid-1]

            if x_mid == len_x:
                x_right_min = math.inf
            else:
                x_right_min = nums1[x_mid]
            if y_sep == 0:
                y_max_left = -math.inf
            else:
                y_max_left = nums2[y_sep-1]
            if y_sep == len_y:
                y_min_right = math.inf
            else:
                y_min_right = nums2[y_sep]

            if x_left_max <= y_min_right and y_max_left <= x_right_min:
                if ((len_x+len_y)%2) == 0:
                    return ((max(x_left_max,y_max_left) + min(x_right_min,y_min_right))/2)
                else:
                    return(max(x_left_max,y_max_left))
            elif x_left_max > y_min_right:
                high_val = x_mid - 1
            else:
                low_val = x_mid + 1