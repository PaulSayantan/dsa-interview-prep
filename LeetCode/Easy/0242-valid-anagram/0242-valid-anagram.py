"""
### Conceptual Breakdown
- Core Algorithmic Pattern: Frequency Counting / Hash Map

- Mental Intuition & Logic:
  1. Anagrams must inherently have the exact same length. If lengths differ, it's impossible for them to be anagrams (Early Exit).
  2. Anagrams must contain the exact same characters with the exact same frequencies. 
  3. Instead of sorting (which takes O(N log N) time), we can count character occurrences in O(N) time.
  4. To optimize space and operations, we can use a single hash map to track the "net balance" of characters. We add 1 for every character found in string `s`, and subtract 1 for every character found in string `t`.
  5. If the strings are valid anagrams, the final frequency balance for every character in the map will be exactly 0.
  
  Note: This dictionary (hash map) approach natively handles the Unicode follow-up question mentioned in the LeetCode editor, unlike a fixed-size array of 26 which only works for lowercase English letters and would cause an IndexError on wider character sets.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines if string t is a valid anagram of string s.
        
        Args:
            s (str): The first input string.
            t (str): The second input string.
            
        Returns:
            bool: True if t is an anagram of s, False otherwise.
            
        Time Complexity: O(N) where N is the length of the strings. We iterate through the strings once.
        Space Complexity: O(K) where K is the number of unique characters. For ASCII, this is O(1) (at most 256). 
                          For Unicode, it scales dynamically up to the number of unique characters present.
        """
        
        # 1. Early Exit: If lengths don't match, they cannot be anagrams.
        if len(s) != len(t):
            return False
            
        # 2. Initialize our frequency map
        char_balance = {}
        
        # 3. Traverse both strings simultaneously
        for i in range(len(s)):
            # Increment balance for characters in 's'
            char_balance[s[i]] = char_balance.get(s[i], 0) + 1
            # Decrement balance for characters in 't'
            char_balance[t[i]] = char_balance.get(t[i], 0) - 1
            
        # 4. Verify that all character balances have resolved to 0
        for count in char_balance.values():
            if count != 0:
                return False
                
        return True

"""
### Reusable Patterns & Key Takeaways
1. The "Net Zero" Strategy: When comparing two collections for equivalence in elements, incrementing counts for collection A and decrementing for collection B allows you to use a single data structure. A valid match always results in a fully zeroed state.
2. Guard Clauses (Early Exits): Always check lengths before processing two strings for anagrams or permutations. It prevents unnecessary O(N) traversal operations.
3. Hash Map vs Fixed Arrays: While a fixed array `[0] * 26` is slightly faster for lowercase English letters, a Hash Map (`dict`) is infinitely more robust for real-world applications dealing with arbitrary Unicode sets, cleanly avoiding out-of-bounds indexing errors.
"""