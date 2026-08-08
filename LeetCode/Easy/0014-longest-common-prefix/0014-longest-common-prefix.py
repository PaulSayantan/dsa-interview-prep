"""
### Conceptual Breakdown
- Core Algorithmic Patterns: Horizontal Scanning, Lexicographical Sorting, String Manipulation.
- Mental Intuition & Logic:
  To find the longest common prefix among an array of strings, the common prefix cannot exceed 
  the length of the shortest string. 
  
  While checking character-by-character across all strings works, there is a powerful intuition 
  tied to sorting: if we sort the array of strings lexicographically (alphabetically), the strings 
  that are most different from one another will naturally be pushed to the first and last positions 
  of the sorted array. 
  
  Therefore, the longest common prefix of the ENTIRE array is simply the longest common prefix 
  between the FIRST and LAST strings in the sorted array. By comparing just these two extremes, 
  we can entirely skip iterating through the middle strings.
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix string amongst an array of strings.

        Args:
            strs (List[str]): A list of strings to be evaluated.

        Returns:
            str: The longest common prefix shared by all strings. Returns an empty 
                 string "" if there is no common prefix or if the input list is empty.

        Time Complexity: O(N log N * M) where N is the number of strings and M is the 
                         maximum string length (due to the string comparison cost during sorting).
        Space Complexity: O(1) auxiliary space (or O(N) depending on the language's sorting 
                          algorithm memory overhead), returning just a slice of the string.
        """
        if not strs:
            return ""

        # Learning Note: Lexicographical sorting organizes strings alphabetically.
        # This guarantees that the strings with the most differing characters will end up
        # at opposite ends of the sorted list.
        strs.sort()

        # Learning Note: By isolating the first and last strings, we reduce an N-string 
        # comparison problem down to a 2-string comparison problem. 
        first_str = strs[0]
        last_str = strs[-1]
        
        # We will build our prefix up to the length of the shorter boundary string.
        max_prefix_len = min(len(first_str), len(last_str))
        
        # Learning Note: Scan horizontally through the two boundary strings.
        for i in range(max_prefix_len):
            if first_str[i] != last_str[i]:
                # Early Exit Strategy: The moment we find a character mismatch between 
                # the two extremes, the common prefix is broken. We immediately slice
                # and return the prefix collected so far.
                return first_str[:i]

        # If the loop finishes without breaking, it means the entire shorter string 
        # is a prefix of the longer string.
        return first_str[:max_prefix_len]


"""
### Reusable Patterns & Key Takeaways

1. The Lexicographical Sorting Trick: 
   When dealing with common prefixes or identifying deviations across a collection of strings, 
   sorting the array lexicographically is a brilliant pattern. It reduces multi-element 
   validation to just comparing the boundaries (index 0 and index n-1).

2. Boundary Evaluation Principle: 
   In problems requiring universal consensus (e.g., "all items must share property X"), 
   evaluating the extremes (min/max or first/last in a sorted sequence) often short-circuits 
   redundant comparisons and massively simplifies the code logic.

3. String Slicing for Immutability: 
   Instead of dynamically appending characters to a list or new string inside a loop (which can 
   incur memory overhead), tracking the matching index and utilizing Python's string slicing 
   (`string[:index]`) at the very end is highly optimal for memory and execution speed.
"""