class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        int m = nums1.length;
        int n = nums2.length;
        int[] mergedarray = new int[m+n];
        
        int i = 0;
        int j = 0;
        int k = 0;
        
        while(i < nums1.length && j < nums2.length) {
            if(nums1[i] < nums2[j]) {
                mergedarray[k++] = nums1[i++];
            } else {
                mergedarray[k++] = nums2[j++];
            }
        }
        
        while(i < nums1.length) {
            mergedarray[k++] = nums1[i++];
        }
        
        while(j < nums2.length) {
            mergedarray[k++] = nums2[j++];
        }
        
        int l = mergedarray.length;
        
        double avg;
        int mid = l/2;
       
        
        if (l%2 == 0) {
            double sum = mergedarray[mid-1] + mergedarray[mid];
            avg = (sum/2); 
        } else {
            avg = (Math.floor(mergedarray[mid]));
        }
        
        return avg;
    }
}