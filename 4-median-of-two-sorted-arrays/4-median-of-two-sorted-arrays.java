class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        if (m > n) return findMedianSortedArrays(nums2, nums1);
        if (m == 0) return (n % 2 == 0)? (nums2[n/2]+nums2[n/2-1])/2.0: nums2[n/2];
        
        int small = 0, big = 0;
        int left = 0, right = m - 1;
        int half = (m+n) / 2;
        while (left < right) {
            int mid1 = left + (right - left) / 2;
            int mid2 = half-2-mid1;
            if (nums1[mid1] <= nums2[mid2+1] && nums2[mid2] <= nums1[mid1+1]) {
                small = Math.max(nums1[mid1], nums2[mid2]);
                big = Math.min(nums1[mid1+1], nums2[mid2+1]);
                if ((n+m) % 2 == 0) return (small+big) / 2.0;
                else return big;
            } else if (nums1[mid1] > nums2[mid2+1]) right = mid1;
            else left = mid1 + 1;
        }
        
        int mid2 = half - 1 - left;
        if (left == 0) {
            if (nums2[mid2] <= nums1[left]) {
                small = nums2[mid2];
                if (mid2 == n - 1 || nums1[left] <= nums2[mid2+1]) big = nums1[left];
                else big = nums2[mid2+1];
            } else {
                big = nums2[mid2];
                if (mid2 == 0 || nums1[left] >= nums2[mid2-1]) small = nums1[left];
                else small = nums2[mid2-1];
            }
        } else {
            if (nums2[mid2] >= nums1[left]) {
                big = nums2[mid2];
                if (mid2 == 0 || nums1[left] >= nums2[mid2-1]) small = nums1[left];
                else small = nums2[mid2-1];
            } else {
                big = nums1[left];
                if (nums2[mid2] >= nums1[left-1]) small = nums2[mid2];
                else small = nums1[left-1];
            }
        }
        return ((m+n) % 2 == 0)? (small+big)/2.0: big;
    }
}