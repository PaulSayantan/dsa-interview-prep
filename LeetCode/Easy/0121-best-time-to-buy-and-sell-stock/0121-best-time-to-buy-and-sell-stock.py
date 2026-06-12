from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Step 1: Initialize trackers
        # min_price tracks the lowest stock price seen so far. 
        # Set to infinity initially so the very first price in the array becomes the minimum.
        min_price = float('inf')
        
        # max_profit tracks the highest profit we can achieve.
        # Initialized to 0 because if no profit can be made (e.g., prices only drop), we return 0.
        max_profit = 0
        
        # Step 2: Iterate through the array exactly once (O(n) time complexity).
        for price in prices:
            
            # Step 3a: Evaluate for a new low.
            # If the current price is lower than our known min_price, 
            # it becomes our new best day to buy. We update min_price.
            if price < min_price:
                min_price = price
            
            # Step 3b: Evaluate for potential profit.
            # If it's not a new minimum, check if selling today yields a better profit.
            # Profit is calculated as the current price minus the lowest historical buy price.
            else:
                current_profit = price - min_price
                
                # If this specific transaction yields more profit than our previous best, 
                # we update max_profit.
                if current_profit > max_profit:
                    max_profit = current_profit
                    
        # Return the ultimate highest profit found. 
        # Space complexity is O(1) because we only used two variables regardless of input size.
        return max_profit