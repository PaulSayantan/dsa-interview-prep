# ============================================================================
# ### Conceptual Breakdown
# ============================================================================
# Core Algorithmic Patterns:
# - Hashing / Hash Map (Dictionary)
# - Frequency Counting (Array/Tuple as a state representation)
#
# Mental Intuition and Logic:
# - Anagrams are words that contain the exact same characters in the exact 
#   same quantities, just in a different order.
# - If we want to group them efficiently, we need a "canonical" (standardized) 
#   way to represent each word so that all anagrams map to the exact same key.
# - Approach 1 (Sub-optimal): Sort each string. "eat", "tea", "ate" all sort 
#   to "aet". We can use "aet" as a hash map key. Sorting takes O(K log K) time 
#   per word (where K is the word length).
# - Approach 2 (Optimal): Count the frequencies of each character. Since the 
#   problem guarantees only lowercase English letters, we can use a fixed-size 
#   array (length 26) to store the count of 'a' through 'z'. We convert this 
#   array to an immutable tuple and use it as our hash map key. Counting takes 
#   O(K) time per word, which is significantly faster for long strings.

from collections import defaultdict
from typing import List

class Solution:
    """
    Groups an array of strings into anagrams using character frequency hashing.

    Time Complexity: O(N * K)
        - N is the number of strings in the input array.
        - K is the maximum length of a string in the array.
        - We iterate through each string and count its characters, avoiding 
          the O(K log K) cost of sorting.
          
    Space Complexity: O(N * K)
        - The hash map stores all the strings and their corresponding keys.
        - In the worst case, every string is unique, leading to N distinct 
          keys of size 26, plus the storage of all N strings of length K.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict with lists. This automatically handles 
        # missing keys by creating an empty list, saving us from checking 
        # if the key exists before appending.
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Create an array of size 26 to store character frequencies.
            # Index 0 corresponds to 'a', 1 to 'b', ..., 25 to 'z'.
            count = [0] * 26
            
            # Iterate through each character in the current string
            for char in s:
                # Calculate the ASCII offset from 'a' to map characters 
                # to their respective indices (0-25).
                count[ord(char) - ord('a')] += 1
            
            # Python dictionaries require immutable keys. A list is mutable, 
            # so we cast the frequency array to a tuple. 
            # All anagrams will generate the exact same tuple.
            anagram_map[tuple(count)].append(s)
            
        # The values of our hash map are the grouped anagrams.
        return list(anagram_map.values())

# ============================================================================
# ### Key Takeaways and Reusable Patterns
# ============================================================================
# 1. Frequency Arrays as Canonical Signatures:
#    Whenever a problem asks you to compare strings ignoring character order 
#    (e.g., anagrams, permutations), a frequency array/hash map is almost 
#    always the optimal identifier.
#
# 2. Immutable Keys in Hash Maps:
#    In Python, lists cannot be used as dictionary keys because they are 
#    mutable (unhashable). Converting state arrays into `tuple(count)` or 
#    strings is a standard pattern for hashing complex states.
#
# 3. collections.defaultdict:
#    Using `defaultdict(list)` instead of a standard `{}` dictionary is an 
#    industry-standard Python pattern to avoid verbose `if key not in dict:` 
#    checks when building lists or accumulating data.
# ============================================================================