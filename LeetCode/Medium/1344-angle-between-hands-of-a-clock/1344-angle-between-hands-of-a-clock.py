class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # STEP 1: Understand the speeds of the hands
        # The minute hand moves 360 degrees in 60 minutes -> 6 degrees/min
        # The hour hand moves 30 degrees in 60 minutes -> 0.5 degrees/min
        
        # STEP 2: Calculate the positions
        # Instead of calculating them separately, we can use the simplified 
        # relative formula derived from absolute difference:
        # | (hour * 30 + minutes * 0.5) - (minutes * 6) |
        # Which simplifies down to: | hour * 30 - 5.5 * minutes |
        
        # We use (hour % 12) so that 12:00 correctly calculates as 0 base degrees 
        # instead of jumping to 360.
        angle = abs((hour % 12) * 30 - 5.5 * minutes)
        
        # STEP 3: Find the smaller angle
        # The hands split the 360-degree circle into two angles. 
        # To find the smaller one, we compare the raw difference with the 
        # remaining outer angle (360 - angle) and return the minimum.
        return min(angle, 360 - angle)