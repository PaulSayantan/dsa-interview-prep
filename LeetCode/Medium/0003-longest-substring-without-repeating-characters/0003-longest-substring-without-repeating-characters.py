class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the most recent index of each character
        char_map = {}
        left = 0
        max_len = 0

        # Iterate through the string with the right pointer
        for right in range(len(s)):
            current_char = s[right]
            
            # If the character is a duplicate AND its last seen index is within the current window
            if current_char in char_map and char_map[current_char] >= left:
                # Instantly move the left pointer to skip the duplicate character
                left = char_map[current_char] + 1
            
            # Update the character's most recent index in the map
            char_map[current_char] = right
            
            # Calculate the current window length and update the maximum length found
            max_len = max(max_len, right - left + 1)

        return max_len