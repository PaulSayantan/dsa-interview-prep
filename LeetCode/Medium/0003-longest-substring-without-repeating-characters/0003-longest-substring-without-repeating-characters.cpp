#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        // Use a vector of size 128 for standard ASCII, initialized to -1
        std::vector<int> charIndex(128, -1);
        
        int left = 0;
        int maxLength = 0;

        // Traverse the string, expanding the window with the right pointer
        for (int right = 0; right < s.length(); ++right) {
            char c = s[right];
            
            // Check if the current character's last seen position is within the active window
            if (charIndex[c] >= left) {
                // Advance the left pointer to immediately resolve the repetition
                left = charIndex[c] + 1;
            }
            
            // Update the dictionary/array with the current character's new index
            charIndex[c] = right;
            
            // Evaluate if the current valid substring is the longest we've seen
            maxLength = std::max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};