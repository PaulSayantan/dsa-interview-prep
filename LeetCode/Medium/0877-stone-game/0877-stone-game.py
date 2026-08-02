class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        GAME THEORY APPROACH (The $O(1)$ Trick):
        
        The problem guarantees two crucial constraints:
        1. There is an EVEN number of piles.
        2. The total sum of stones is ODD (meaning no ties are possible).

        Because the number of piles is even, we can group them by their original 
        array indices into two distinct sets: 
        - Even-indexed piles: 0, 2, 4, 6...
        - Odd-indexed piles:  1, 3, 5, 7...
        
        Since the total sum of all stones is odd, the sum of the even-indexed set 
        and the sum of the odd-indexed set can never be equal. One set will ALWAYS 
        contain more stones than the other.

        HOW ALICE FORCES A WIN:
        Because Alice goes first, she has the power to decide which set she wants, 
        and she can completely lock Bob out of that set. 
        
        If Alice decides she wants all the Even-indexed piles:
        - She starts by picking `piles[0]` (an Even index).
        - The remaining piles now range from index 1 to n-1. Both ends of the remaining 
          piles are now Odd indices.
        - No matter which end Bob picks from, he is forced to take an Odd-indexed pile, 
          which simultaneously exposes the next Even-indexed pile for Alice's next turn.
        
        Alice simply calculates which set (Even or Odd) has a higher total sum before 
        the game begins, and plays the strategy to collect only from that set. Bob is 
        powerless to stop her.

        ---------------------------------------------------------------------------
        EXAMPLE WALKTHROUGH:
        piles = [5, 3, 4, 5]
        Indices: 0  1  2  3
        
        1. Calculate Sets:
           Even-indexed sum: piles[0] + piles[2] = 5 + 4 = 9
           Odd-indexed sum:  piles[1] + piles[3] = 3 + 5 = 8
        
        2. Alice's Choice:
           Alice knows 9 > 8, so she decides to take only Even-indexed piles (indices 0 and 2).
        
        3. Gameplay:
           - Turn 1 (Alice): Takes `piles[0]` (5). 
             Remaining array: [3, 4, 5] (Original indices: 1, 2, 3)
             
           - Turn 2 (Bob): Is forced to pick from the ends (index 1 or index 3).
             
             Scenario A (Bob takes left): 
             Bob picks `piles[1]` (3). Remaining: [4, 5] (Indices: 2, 3).
             Alice takes `piles[2]` (4). 
             Result: Alice = 5 + 4 = 9. Bob gets the rest. Alice wins.
             
             Scenario B (Bob takes right): 
             Bob picks `piles[3]` (5). Remaining: [3, 4] (Indices: 1, 2).
             Alice takes `piles[2]` (4). 
             Result: Alice = 5 + 4 = 9. Bob gets the rest. Alice wins.
                      
        Because Alice can always perfectly execute this strategy under these constraints, 
        she will mathematically never lose.
        """
        return True