class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Pointer 1 (p1): Points to the last valid element in nums1
        p1 = m - 1
        
        # Pointer 2 (p2): Points to the last element in nums2
        p2 = n - 1
        
        # Pointer for insertion (p_insert): Points to the last empty slot in nums1
        p_insert = m + n - 1
        
        # Step 1: Compare elements from the back and place the larger one at p_insert
        # We only do this as long as both arrays have elements left to compare.
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                # If nums1's element is larger, place it at the insertion point
                nums1[p_insert] = nums1[p1]
                p1 -= 1
            else:
                # If nums2's element is larger (or equal), place it at the insertion point
                nums1[p_insert] = nums2[p2]
                p2 -= 1
                
            # Move the insertion pointer backward after every placement
            p_insert -= 1
            
        # Step 2: Handle remaining elements in nums2
        # If p1 < 0, it means nums1 was exhausted first. We must copy the rest of nums2.
        # (If p2 < 0, nums2 was exhausted first, and the remaining nums1 elements 
        # are already in their correct places at the front of the array, so we do nothing).
        while p2 >= 0:
            nums1[p_insert] = nums2[p2]
            p2 -= 1
            p_insert -= 1