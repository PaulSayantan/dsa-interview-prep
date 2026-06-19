#include <vector>

class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        
        // 1. Initialize Pointers: Setup the read pointers (p1, p2) and write pointer (pInsert)
        int p1 = m - 1;
        int p2 = n - 1;
        int pInsert = m + n - 1;
        
        // 2. Compare and Insert: Evaluate the maximums at the back, placing them at pInsert
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
        
        // 3. Handle Leftovers: If nums1 runs out, copy the remainder of nums2
        while (p2 >= 0) {
            nums1[pInsert] = nums2[p2];
            p2--;
            pInsert--;
        }
    }
};