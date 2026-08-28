class Solution:
    """
    ===========================================================================
    137. Single Number II - Educational Guide
    ===========================================================================
    
    ### Conceptual Breakdown
    
    - Core Algorithmic Pattern: Bit Manipulation / State Machine (Digital Logic)
    
    - Mental Intuition:
      The standard XOR trick (used in Single Number I) works beautifully when 
      duplicates appear exactly twice because XORing a number with itself 
      cancels it out (a ^ a = 0). 
      
      However, in this problem, duplicates appear exactly THREE times. A simple 
      XOR will leave you with a ^ a ^ a = a, mixing the repeating numbers with 
      the unique target number. We need a bitwise operation that resets to 0 
      after exactly THREE occurrences.
      
      Think of this as building a state machine for every single bit position (0 to 31) 
      simultaneously. Each bit can be in one of three states:
      1. Seen exactly once.
      2. Seen exactly twice.
      3. Seen exactly three times (which should immediately reset to 0).
      
    - The Logic:
      To track three states, a single binary variable isn't enough (it only 
      holds 0 or 1). We need TWO variables to act as our bit counters:
      * `ones`: Tracks bits that have appeared exactly 1 time (or 4, 7, etc.).
      * `twos`: Tracks bits that have appeared exactly 2 times (or 5, 8, etc.).
      
      When a bit appears for the first time, we add it to `ones`.
      When it appears for the second time, we remove it from `ones` and add it to `twos`.
      When it appears for the third time, it gets removed from `twos` and resets to 0.
      
      By the end of the array, `ones` will hold exactly the bits of the number 
      that appeared only once.
    """

    def singleNumber(self, nums: list[int]) -> int:
        """
        Finds the element that appears exactly once in an array where every 
        other element appears exactly three times.

        Args:
            nums (list[int]): An array of integers.

        Returns:
            int: The single integer that does not repeat.
        """
        ones = 0
        twos = 0
        
        for num in nums:
            # Step 1: Update `ones`
            # (ones ^ num): Add the new bits from `num` to `ones`. If a bit was 
            #               already in `ones`, this removes it (state 1 -> state 2).
            # & ~twos:      However, if this bit is ALREADY in `twos` (meaning it's 
            #               appearing for the 3rd time), we must NOT add it to `ones`. 
            #               The `& ~twos` acts as a guard blocking 3rd appearances.
            ones = (ones ^ num) & ~twos
            
            # Step 2: Update `twos`
            # (twos ^ num): Add the new bits to `twos`. If a bit was already in 
            #               `twos` (3rd appearance), this removes it (state 2 -> state 0).
            # & ~ones:      However, if the bit just got added to `ones` in Step 1 
            #               (meaning it's a 1st appearance), we must NOT add it to `twos`.
            #               The `& ~ones` acts as a guard blocking 1st appearances.
            twos = (twos ^ num) & ~ones
            
        # At the end, the unique number has appeared exactly once, 
        # so its bits are safely stored in `ones`.
        return ones

    """
    ===========================================================================
    Summary of Reusable Patterns & Key Takeaways
    ===========================================================================
    
    1. Bitwise State Machines: When counting occurrences of elements up to a 
       limit $K$ in $O(1)$ space, you can use $\log_2(K)$ integer variables 
       to act as a counter for the bits.
       
    2. The "Filter" Pattern (`& ~mask`): Using `& ~variable` is a powerful 
       way to conditionally block bits from being set. It reads as "AND NOT 
       in variable". We used it here to ensure a bit can't be in both `ones` 
       and `twos` at the same time.
       
    3. Performance: While a 32-bit nested loop (checking each bit position 
       manually) works and is technically $O(32N) \rightarrow O(N)$, this 
       state machine approach reduces it to a pure, single-pass $O(N)$ with 
       no loop overhead, making it the mathematically optimal solution. Furthermore,
       it completely avoids Python's arbitrary-precision integer issues with 
       two's complement negative numbers that the 32-bit loop method struggles with.
    """