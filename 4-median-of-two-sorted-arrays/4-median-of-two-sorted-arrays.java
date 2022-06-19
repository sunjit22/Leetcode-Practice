class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // write your code here
        int len = nums1.length + nums2.length;
        if (len % 2 == 1) {
            return finKth(nums1, 0, nums2, 0, len / 2 + 1);
        } else {
            return (
                finKth(nums1, 0, nums2, 0, len / 2) + finKth(nums1, 0, nums2, 0, len / 2 + 1)
                ) / 2.0;
        }
    }
    
    private double finKth(int[] nums1, int indA, int[] nums2, int indB, int k) {
        if (indA >= nums1.length) {
            return nums2[indB + k - 1];
        }
        if (indB >= nums2.length) {
            return nums1[indA + k - 1];
        }
        if (k == 1) {
            return Math.min(nums1[indA], nums2[indB]);
        }
        
        int A_key = indA + k / 2 - 1 < nums1.length 
                    ? nums1[indA + k / 2 - 1]
                    : Integer.MAX_VALUE;
        int B_key = indB + k / 2 - 1 < nums2.length
                    ? nums2[indB + k / 2 - 1]
                    : Integer.MAX_VALUE;
        if (A_key > B_key) {
            return finKth(nums1, indA, nums2, indB + k / 2, k - k / 2);
        } else {
            return finKth(nums1, indA + k / 2, nums2, indB, k - k / 2);
        }
    }
}