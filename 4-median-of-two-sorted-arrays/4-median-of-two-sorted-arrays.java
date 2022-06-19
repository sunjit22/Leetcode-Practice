class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
int len1=nums1.length;//Taking lengths of the numbers considered.
        int len2=nums2.length;//Similaryly for len2
        int i1=0, i2=0;
        int s=(len1+len2)/2;
        int[] a = new int[s+1];//Taking in the form of array
        for(int i=0 ; i<a.length ; i++) {
            if(i1<nums1.length && i2<nums2.length) {//Checking whether i1 and i2 are less than respective lengths of numbers.
                if(nums1[i1]<=nums2[i2]) {
                    a[i] = nums1[i1++];
                } else {
                    a[i] = nums2[i2++];
                }
            } else {
                if(i1<nums1.length) {
                    a[i] = nums1[i1++];
                } else {
                    a[i] = nums2[i2++];
                }
            }
        }
        return (a[(len1+len2-1)/2] + a[(len1+len2)/2])/2.0;//returing the output if above cases run successfully
        
    }
}