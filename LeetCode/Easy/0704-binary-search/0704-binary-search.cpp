#include <vector>

class Solution {
public:
    /**
     * Intuition:
     * When data is organized and sorted sequentially, searching sequentially is inefficient. 
     * By inspecting the central element of our current window, we obtain definitive information 
     * about where the target lies relative to that point. This cuts our workload in half 
     * exponentially.
     * * Approach:
     * - Establish a search window using 'low' and 'high' indices.
     * - Continuously narrow down this window by calculating a dynamic 'mid' element.
     * - Update bounds using 'mid + 1' or 'mid - 1' to avoid getting stuck in infinite loops 
     * and to ensure strict reduction of the search zone.
     * - Return the index instantly upon a successful match, or yield -1 if the bounds cross.
     * * Complexity Analysis:
     * - Time Complexity: O(log n) -> The array size shrinks geometrically ($N, N/2, N/4, \dots$).
     * - Space Complexity: O(1)   -> Standard iterative approach requires no recursive stack frames.
     */
    int search(std::vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        
        while (low <= high) {
            // Protects against signed integer overflow conditions
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) {
                return mid;
            }
            else if (nums[mid] < target) {
                low = mid + 1;
            }
            else {
                high = mid - 1;
            }
        }
        
        return -1;
    }
};