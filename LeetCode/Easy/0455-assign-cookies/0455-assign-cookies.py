class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # Step 1: Sort both the greed factors (g) and the cookie sizes (s).
        # This is the foundation of our Greedy approach. By sorting, we ensure
        # that we always try to satisfy the least greedy child first, and we 
        # try to do it using the smallest cookie possible to minimize waste.
        g.sort()
        s.sort()
        
        # Step 2: Initialize two pointers. 
        # 'child_i' tracks the current child we are trying to satisfy.
        # 'cookie_j' tracks the current cookie we are evaluating to give out.
        child_i = 0
        cookie_j = 0
        
        # Step 3: Iterate as long as we still have both children and cookies to check.
        # If child_i reaches the end of g, all children are happily satisfied.
        # If cookie_j reaches the end of s, we have completely run out of cookies.
        while child_i < len(g) and cookie_j < len(s):
            
            # Step 3a: Check if the current cookie is big enough for the current child.
            if s[cookie_j] >= g[child_i]:
                
                # The cookie is big enough! The child is content.
                # We move the child pointer forward to look at the next child.
                child_i += 1
            
            # Step 3b: Move to the next cookie regardless of the outcome.
            # If the cookie was used (Step 3a), we must move on to a fresh cookie.
            # If the cookie was TOO SMALL, we also move on. Since 'g' is sorted, 
            # if this cookie is too small for the current child, it will definitely 
            # be too small for all the greedier children left in the line.
            cookie_j += 1
            
        # Step 4: Return the result.
        # Because we only increment 'child_i' when a child successfully gets a cookie,
        # the value of 'child_i' naturally represents the total number of content children.
        return child_i