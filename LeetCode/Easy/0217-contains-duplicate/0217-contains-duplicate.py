class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Hash Set Approach.
        
        Intuition:
        We can trade a little bit of memory for speed. By keeping track of the 
        elements we've already seen in a Hash Set, we can check if a number 
        is a duplicate in instant O(1) time as we loop through the list.
        
        Complexity:
        - Time Complexity: O(N) because looking up and adding elements to a set takes O(1) on average.
        - Space Complexity: O(N) to store the elements in the set.
        """
        seen = set()
        
        for num in nums:
            if num in seen:
                return True  # Found a duplicate!
            seen.add(num)
            
        return False  # All elements are unique