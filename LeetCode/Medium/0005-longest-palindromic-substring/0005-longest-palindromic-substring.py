class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in a given string.
        
        METHODOLOGY: Expand Around Center
        Instead of checking every possible substring (which takes O(n^3)), 
        we iterate through each character in the string and expand outwards.
        Because a palindrome mirrors around its center, we can validate a 
        palindrome in O(n) time from the inside out.
        
        TIME COMPLEXITY: O(n^2)
        - We visit each character in the string of length n: O(n)
        - For each character, the while loops can expand up to n times: O(n)
        - Total time = O(n) * O(n) = O(n^2)
        
        SPACE COMPLEXITY: O(1)
        - We only store a few pointer variables and the string slice 
          (ignoring the memory allocated for the final return string).
        """
        
        # Edge case: If the string is empty or length 1, it is inherently a palindrome.
        if not s or len(s) <= 1:
            return s

        def expand_around_center(left: int, right: int) -> str:
            """
            Helper function to expand outward from a given center.
            
            :param left: The starting left index of the center.
            :param right: The starting right index of the center.
            :return: The longest valid palindrome string from this center.
            """
            # Continue expanding outward as long as:
            # 1. We stay within the string boundaries (left >= 0, right < len(s))
            # 2. The characters at the left and right pointers match.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            # Once the loop breaks, s[left] != s[right]. 
            # The valid palindrome is strictly *inside* the current left and right bounds.
            # We add 1 to 'left' to exclude the invalid character.
            # Python's slicing [start:end] is exclusive at the 'end', so 'right' is inherently excluded.
            return s[left + 1:right]

        longest_palindrome = ""

        # Iterate through every character in the string, treating it as a center.
        for i in range(len(s)):
            # Case 1: Odd length palindromes (e.g., "aba")
            # The center is exactly at index i.
            odd_pal = expand_around_center(i, i)
            
            # Case 2: Even length palindromes (e.g., "abba")
            # The center is strictly *between* index i and i+1.
            even_pal = expand_around_center(i, i + 1)
            
            # Compare the newly found palindromes with the longest one found so far.
            # The max() function with key=len evaluates the strings by their length.
            longest_palindrome = max(longest_palindrome, odd_pal, even_pal, key=len)

        return longest_palindrome

"""
================================================================================
REUSABLE PATTERNS & KEY TAKEAWAYS
================================================================================

1. THE "EXPAND AROUND CENTER" PATTERN:
   - Use this pattern whenever a problem asks about substrings that mirror 
     themselves (Palindromes, concentric string matching).
   - ALWAYS account for both Odd-Length (1 character center) and Even-Length 
     (2 character center) possibilities.

2. AVOIDING DYNAMIC PROGRAMMING OVERKILL:
   - DP is a standard solution for string subset problems, but a 2D DP matrix
     for palindromes requires O(n^2) auxiliary space. 
   - Before committing to DP, ask yourself: "Can I simulate this optimally 
     using two pointers?" If yes, you can usually drop space complexity to O(1).

3. PYTHON STRING SLICING BOUNDARIES:
   - When pointers cross or stop at invalid characters (as in the while loop 
     above), remember that standard Python slicing `string[start:end]` includes 
     `start` but excludes `end`. 
   - If pointers `left` and `right` sit on invalid characters, the valid slice 
     is `string[left + 1 : right]`.

4. THE MAX() FUNCTION TRICK:
   - Python's `max()` function can take multiple arguments and a custom `key`.
     Using `max(str1, str2, str3, key=len)` is a clean, Pythonic way to avoid 
     writing multiple nested `if/elif` length comparison blocks.
================================================================================
"""