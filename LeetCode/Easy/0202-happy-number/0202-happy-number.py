class Solution:
    def isHappy(self, n: int) -> bool:
        # A hash set to keep track of the numbers we have already seen.
        # This allows us to detect endless cycles in O(1) average time.
        tracked_numbers = set()
        
        # Continuously transform the number until it hits 1 (Happy)
        # or we detect a cycle (Unhappy).
        while n != 1:
            current_sum = 0
            
            # Extract digits and calculate the sum of their squares
            while n > 0:
                digit = n % 10          # Get the rightmost digit
                current_sum += digit ** 2 # Square it and add to total
                n = n // 10             # Remove the rightmost digit
                
            # If the new sum has been seen before, we are trapped in an endless loop
            if current_sum in tracked_numbers:
                return False
                
            # Document this new number and update 'n' for the next iteration
            tracked_numbers.add(current_sum)
            n = current_sum
            
        # If the loop exits naturally, n reached 1
        return True