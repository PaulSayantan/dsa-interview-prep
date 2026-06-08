class Solution:
    def isValid(self, s: str) -> bool:
        """
        ==================================================================
        PROBLEM: 20. Valid Parentheses
        ==================================================================
        
        INTUITION:
        The problem requires us to verify if brackets are closed in the correct 
        order and matched with their corresponding pairs. A key observation is 
        that the last opened bracket must be the first one to be closed. For 
        example, in "([])", the '[' is opened last, so it must meet its matching 
        ']' first before we can close the outer '('.
        
        This "Last-In, First-Out" (LIFO) behavior perfectly mirrors the Stack 
        data structure. 
        
        APPROACH:
        1. Use a hash map (dictionary) to map each opening bracket to its 
           corresponding closing bracket. This makes pairing checks $O(1)$.
        2. Initialize an empty list to act as our `stack`.
        3. Iterate through each character `ch` in the string `s`:
           - If `ch` is an opening bracket (exists as a key in our map), 
             we push (append) it onto our stack.
           - If `ch` is a closing bracket, we check if the stack has an opening 
             bracket waiting. 
             - If the stack is empty, it means we have an unmatched closing 
               bracket (e.g., s = "]"), so we immediately return False.
             - If the stack is not empty, we pop the top element and check if 
               its matching closing bracket matches `ch`. If it doesn't, 
               the string is invalid, so we return False.
        4. After the loop, if the stack is completely empty, it means all 
           opening brackets were successfully matched and closed. If anything 
           remains in the stack (e.g., s = "(()"), it's invalid.
           
        COMPLEXITY ANALYSIS:
        - Time Complexity: $O(n)$ where $n$ is the length of the string. We 
          traverse the string exactly once, and stack push/pop operations 
          take $O(1)$ time.
        - Space Complexity: $O(n)$ because in the worst-case scenario (e.g., 
          s = "((((("), we might push all characters onto the stack.
        ========================================================================
        """
        # Dictionary to quickly map and validate bracket pairs
        bracket_map = {'(': ')', '{': '}', '[': ']'}
        stack = []
        
        for ch in s:
            # If it's an opening bracket, push it to the stack
            if ch in bracket_map:
                stack.append(ch)
            # If it's a closing bracket
            else:
                # If stack is empty, there is no opening bracket to match this closing one
                if not stack:
                    return False
                
                # Pop the last opening bracket and check if it matches the current closing one
                last_open = stack.pop()
                if bracket_map[last_open] != ch:
                    return False
                    
        # If the stack is empty, all brackets were paired correctly
        return len(stack) == 0
