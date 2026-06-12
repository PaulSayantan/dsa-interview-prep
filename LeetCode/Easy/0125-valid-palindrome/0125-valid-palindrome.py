class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: 'left' at the start and 'right' at the end
        left, right = 0, len(s) - 1
        
        # Continue checking as long as the left pointer is before the right pointer
        while left < right:
            
            # Move the 'left' pointer forward if the current character is NOT alphanumeric
            # We also ensure left < right to prevent out-of-bounds errors
            while left < right and not s[left].isalnum():
                left += 1
                
            # Move the 'right' pointer backward if the current character is NOT alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare the valid characters at both pointers (converted to lowercase)
            # If they are different, the string is not a palindrome
            if s[left].lower() != s[right].lower():
                return False
            
            # If they match, move both pointers inward to check the next set of characters
            left += 1
            right -= 1
            
        # If the loop finishes without returning False, the string reads the same forward and backward
        return True