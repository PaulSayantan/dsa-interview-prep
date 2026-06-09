class Solution {
    public boolean isHappy(int n) {
        /*
         * INTUITION & THOUGHT PROCESS:
         * 1. This problem asks us to repeatedly replace a number with the sum of the squares 
         * of its digits. This process will either terminate at 1 (Happy) or loop infinitely (Unhappy).
         *
         * * 2. Why does it loop instead of growing to infinity?
         * Even for a massive number like 999,999,999, the sum of the squares of its digits 
         * is 9 * (9^2) = 729. Large numbers shrink incredibly fast, dropping into a small, 
         * finite range (below 243). Because the range is finite, numbers MUST eventually repeat.
         *
         * * 3. Graph/Linked List Analogy:
         * If we treat each number as a "node" and the transition to the next sum as a "next pointer", 
         * this problem maps perfectly to finding a cycle in a Singly Linked List.
         * - A Happy Number is a linked list that terminates in a single-node loop at 1 (1 -> 1 -> 1).
         * - An Unhappy Number is a linked list that gets trapped in a larger cyclic loop.
         *
         * * 4. Optimization (Floyd's Cycle-Finding Algorithm):
         * Instead of using a Hash Set which costs O(log n) auxiliary memory to remember seen numbers, 
         * we can use the "Tortoise and the Hare" approach. 
         * - We track two pointers moving at different speeds.
         * - The 'slow' pointer (Tortoise) moves 1 step at a time.
         * - The 'fast' pointer (Hare) moves 2 steps at a time.
         * - If there is a cycle, the fast pointer will eventually lap the slow pointer and they 
         * will meet (slow == fast). If there is no cycle, the fast pointer will reach 1 first.
         *
         * * SPACE COMPLEXITY: O(1) - Consumes absolute constant space.
         * * TIME COMPLEXITY:  O(log n) - Bounded by the digit extraction of the initial number.
         */

        // Initialize the slow pointer at the starting number
        int slow = n;
        // Initialize the fast pointer 1 step ahead
        int fast = getNext(n);
        
        // Loop runs as long as the fast pointer hasn't hit 1 (not yet confirmed happy)
        // AND the two pointers haven't collided (no cycle detected yet)
        while (fast != 1 && slow != fast) {
            slow = getNext(slow);         // Tortoise moves 1 step ahead
            fast = getNext(getNext(fast)); // Hare moves 2 steps ahead
        }
        
        // If the loop broke because fast reached 1, it's a happy number (returns true).
        // If it broke because slow == fast at a number other than 1, a cycle exists (returns false).
        return fast == 1;
    }

    /**
     * Helper method to calculate the "next node" in our implicit linked list.
     * It extracts digits from right to left, squares them, and sums them up.
     */
    private int getNext(int num) {
        int totalSum = 0;
        
        while (num > 0) {
            int digit = num % 10;     // Extract the rightmost digit (modulo 10)
            totalSum += digit * digit; // Square the digit and add to the running total
            num /= 10;                // Chop off the rightmost digit (integer division by 10)
        }
        
        return totalSum;
    }
}