class Solution:
    def hammingWeight(self, n: int) -> int:
        # 1. Initialize a Tracker: Keep track of the number of '1's found.
        count = 0
        
        # 2. Establish the Condition: Loop continues as long as there are still '1' bits (n != 0).
        while n:
            # 3. Apply the Bit Trick: n & (n - 1) flips the rightmost '1' bit to '0'.
            # This effectively strips one '1' off the binary representation per iteration.
            n = n & (n - 1)
            
            # 4. Increment: Since we successfully stripped a '1', we increase our tally.
            count += 1
            
        # 5. Return the Result: Once n is 0, all '1's have been counted.
        return count