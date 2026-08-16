"""
### Conceptual Breakdown

Core Algorithmic Patterns:
- Two Pointers (Opposite Directional / Converging Pointers)
- In-place Data Traversal / Filtering

Mental Intuition & Logic:
The defining characteristic of a palindrome is symmetry: it reads the same forwards and 
backwards. A brute-force or naive approach would be to iterate through the string, build 
a new filtered string containing only lowercased alphanumeric characters, and then compare 
it to its reverse. While this works, it requires O(N) extra space to store the new string.

To reach the optimal O(1) space complexity, we must evaluate the string in-place without 
allocating memory for a new string. We can achieve this by utilizing the Two-Pointer pattern:
1. Place one pointer at the start (left) and one at the end (right) of the string.
2. Move the pointers towards the center simultaneously.
3. If the 'left' pointer encounters a non-alphanumeric character, advance it inward 
   until it finds a valid character.
4. Do the same for the 'right' pointer.
5. Once both pointers are resting on valid alphanumeric characters, compare them 
   (ignoring case). If they mismatch, the symmetry is broken, and we return False.
6. If they match, move both pointers inward and repeat.
7. If the pointers meet or cross without encountering a mismatch, the string is symmetric.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Checks if a given string is a valid palindrome, considering only 
        alphanumeric characters and ignoring cases.

        Args:
            s (str): The input string to be evaluated.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        
        Complexity:
            Time: O(N) where N is the length of the string. In the worst case, 
                  each character is visited at most once by the pointers.
            Space: O(1) because we only allocate two integer variables for our 
                   pointers, regardless of the input string's size.
        """
        # Initialize two pointers at the absolute boundaries of the string
        left, right = 0, len(s) - 1
        
        # Continue evaluating as long as the pointers haven't crossed paths
        while left < right:
            
            # Skip any invalid characters from the left side.
            # The 'left < right' check prevents Out-Of-Bounds errors if the string 
            # contains only symbols (e.g., "   ").
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip any invalid characters from the right side.
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Both pointers are now on alphanumeric characters. 
            # Compare them in lowercase to ensure case-insensitivity.
            if s[left].lower() != s[right].lower():
                return False
            
            # If they match, step both pointers inward to check the next pair
            left += 1
            right -= 1
            
        # All valid character pairs matched successfully
        return True


"""
### Reusable Patterns & Key Takeaways

1. Converging Pointers for Symmetry: 
   Whenever you are tasked with checking for symmetry (like palindromes) or finding pairs 
   that satisfy a condition in a sorted array (like Two Sum II), placing pointers at 
   opposite ends and moving them inward is the gold standard for O(N) time and O(1) space.

2. In-Place Filtering: 
   Instead of spending memory to create a "clean" version of your data structure before 
   processing it, embed the skipping/filtering logic directly into your traversal loop 
   (e.g., `while not valid: pointer += 1`). This is crucial for optimizing space complexity.

3. String Utilities vs. ASCII Math: 
   Leveraging built-in language utilities like Python's `isalnum()` and `lower()` keeps code 
   clean and readable. However, it is always beneficial to remember the underlying ASCII logic 
   as a fallback for older languages or strict interviewers (e.g., checking if a character 
   falls within 'a'-'z', 'A'-'Z', or '0'-'9').
"""