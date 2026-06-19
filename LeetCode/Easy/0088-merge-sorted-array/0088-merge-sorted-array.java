class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
        // 1. Initialize Pointers: Setup pointers for the ends of valid data and the end of the container.
        int p1 = m - 1;
        int p2 = n - 1;
        int pInsert = m + n - 1;
        
        // 2. Compare and Insert: Compare from the back to safely modify nums1 in-place.
        while (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] > nums2[p2]) {
                nums1[pInsert] = nums1[p1];
                p1--;
            } else {
                nums1[pInsert] = nums2[p2];
                p2--;
            }
            pInsert--;
        }
        
        // 3. Handle Leftovers: Sweep up any remaining elements in nums2.
        while (p2 >= 0) {
            nums1[pInsert] = nums2[p2];
            p2--;
            pInsert--;
        }
    }
}