class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        PROBLEM PATTERN: 
        This is a classic "Modified Binary Search" on a rotated sorted array.
        Normally, binary search requires a fully sorted array. However, a rotated 
        sorted array has a special property: if you divide it in half, AT LEAST ONE 
        half will always be strictly sorted.
        
        INTUITION:
        1. Find the mid-point.
        2. Identify which half (left or right) is sorted.
        3. The minimum element of a sorted half is ALWAYS its first element. 
           We take that minimum, store it, and then discard that half because we 
           already know its lowest possible value.
        4. We then search the OTHER, unsorted half for an even smaller element.
        """
        
        low, high = 0, len(nums) - 1

        # early exit incase the array is not rotated at all
        if nums[low] <= nums[high]:
            return nums[low]
        
        # Use float('inf') instead of a hardcoded magic number like 9999.
        # This ensures the code works universally regardless of input constraints.
        ans = float('inf') 
        
        while low <= high:
            # OPTIMIZATION:
            # If the value at 'low' is less than or equal to the value at 'high',
            # the current sub-array is perfectly sorted (no rotation in this segment).
            # The smallest element here is just nums[low].
            if nums[low] <= nums[high]:
                ans = min(ans, nums[low])
                break # We can stop searching entirely.
            
            # Calculate mid-point. Using // for integer division.
            mid = (low + high) // 2
            
            # CODING APPROACH: Identify the sorted half.
            
            # Case 1: The Left Half is sorted.
            # (Notice the <= to handle cases where low == mid)
            if nums[low] <= nums[mid]:
                # Since it's sorted, the smallest value in this half is nums[low].
                # We update our answer with this potential minimum.
                ans = min(ans, nums[low])
                
                # We've processed the left half, so the absolute minimum must 
                # be hiding in the right half. Move the 'low' pointer.
                low = mid + 1
                
            # Case 2: The Right Half is sorted.
            else:
                # Since it's sorted, the smallest value in this right half is nums[mid].
                # Update our answer.
                ans = min(ans, nums[mid])
                
                # We've processed the right half, so we move our search to the left half.
                high = mid - 1
                
        return ans