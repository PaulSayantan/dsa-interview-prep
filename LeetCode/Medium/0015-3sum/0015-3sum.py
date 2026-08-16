"""
### Conceptual Breakdown
- Core Algorithmic Patterns: Sorting, Two Pointers (Anchor + Sliding Window).
- Mental Intuition & Logic: 
  The naive approach to finding three numbers that sum to zero requires three nested 
  loops, resulting in an O(N^3) time complexity. To optimize this, we can sort the 
  array first. Sorting provides two massive benefits:
  
  1. Deduplication: The problem requires distinct triplets. Sorting groups identical 
     elements together, making it trivial to skip them by checking adjacent values, 
     thus avoiding duplicate triplets in our result set without needing a Hash Set.
     
  2. Directional Search (Two Pointers): By iterating through the array and fixing one 
     number (the anchor), we reduce the problem to the classic "Two Sum II" problem 
     (Two Sum on a sorted array). We can then use a left pointer (starting just after 
     the anchor) and a right pointer (starting at the end of the array) to find the 
     remaining two numbers. Because the array is sorted, we know exactly which pointer 
     to move if our sum is too large or too small. This reduces the search time for 
     the remaining two elements to O(N), bringing total time complexity down to O(N^2).
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Finds all unique triplets in the array which gives the sum of zero.
        
        Args:
            nums (list[int]): A list of integers.
            
        Returns:
            list[list[int]]: A list of lists, where each inner list contains 
                             a unique triplet that sums to zero.
                             
        Time Complexity: O(N^2) where N is the number of elements in nums.
        Space Complexity: O(1) or O(N) depending on the sorting algorithm's 
                          underlying memory usage.
        """
        # Step 1: Sort the array to handle duplicates and enable the two-pointer approach.
        nums.sort()
        res = []
        n = len(nums)
        
        # Step 2: Iterate through the array, using each number as an anchor.
        # We can stop 2 elements early because we need at least 3 elements for a triplet.
        for i in range(n - 2):
            
            # OPTIMIZATION: If the smallest number in our remaining window is greater 
            # than 0, no three numbers can sum to 0. We can safely terminate early.
            if nums[i] > 0:
                break
                
            # DEDUPLICATION (Anchor): Skip duplicate anchor values to prevent evaluating 
            # the same starting number multiple times.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Step 3: Initialize two pointers for the remaining window.
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Triplet found. Add to results.
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Advance both pointers to look for other valid pairs 
                    # for the same anchor.
                    left += 1
                    right -= 1
                    
                    # DEDUPLICATION (Pointers): Skip duplicate values for the left pointer 
                    # to avoid duplicate combinations.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    # Skip duplicates for the right pointer too (optional but efficient).
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif current_sum < 0:
                    # Sum is too small. Since the array is sorted, we need a larger 
                    # number, so we move the left pointer to the right.
                    left += 1
                else:
                    # Sum is too large. We need a smaller number, so we move the 
                    # right pointer to the left.
                    right -= 1
                    
        return res

"""
### Reusable Patterns & Key Takeaways
1. Sort + Two Pointers: 
   Whenever a problem asks to find pairs, triplets, or quads that meet a specific sum 
   or condition (and returning indices is NOT required), sorting the input array is 
   almost always the optimal first step. It unlocks O(N) two-pointer traversals.

2. Deduplication through Sorting: 
   Sorting brings identical elements adjacent to one another. You can easily skip 
   duplicates in a `for` or `while` loop by simply checking `arr[i] == arr[i - 1]`. 
   This is far more space-efficient than using sets to filter duplicates later.

3. Early Termination: 
   In sorted arrays, you can often establish absolute boundaries. For instance, if 
   you are looking for a sum of 0 and your smallest number is > 0, you can `break` 
   immediately, saving unnecessary loop cycles.

4. Complexity Shift: 
   Transforming O(N^3) to O(N log N) [for sorting] + O(N^2) [for traversing] equals 
   a final time complexity of O(N^2). This "anchor + 2-pointer" reduction is a staple 
   for k-Sum problems.
"""