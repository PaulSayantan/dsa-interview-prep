/**
 * ### Conceptual Breakdown
 * 
 * Pattern: Data Structure Design, State Tracking, Stack (LIFO)
 * 
 * Mental Intuition & Logic:
 * The primary challenge of a Min Stack is that standard stacks support O(1) 
 * insertions and deletions, but finding a minimum typically requires an O(N) scan. 
 * Furthermore, if the current minimum element is popped, the stack must instantly "remember" 
 * what the previous minimum was.
 * 
 * To solve this in O(1) time, we must track the state of the minimum value 
 * *at every single level* of the stack. Instead of storing just the raw value, 
 * we store a custom Node: the value itself, and the minimum value of the entire 
 * stack at the exact moment this element was added.
 * 
 * By using a dynamically allocated Linked List structure, we overcome the brittleness 
 * of hardcoded array limits (like MAX_SIZE = 30000 seen in array implementations) 
 * while maintaining strict O(1) time complexity for all operations.
 */
class MinStack {

    /**
     * Internal Node class to represent each element in the stack.
     * Acts as a Linked List node, tracking the value, the current minimum, 
     * and a reference to the previous top of the stack.
     */
    private class Node {
        int val;
        int min;
        Node next;
        
        /**
         * Constructs a new stack node.
         * 
         * @param val  The integer value to push onto the stack.
         * @param min  The minimum value in the stack up to this current node.
         * @param next Reference to the next node (the previous top of the stack).
         */
        private Node(int val, int min, Node next) {
            this.val = val;
            this.min = min;
            this.next = next;
        }
    }
    
    // Pointer to the top of the stack
    private Node head;

    /** 
     * Initializes the stack object. 
     */
    public MinStack() {
        head = null;
    }
    
    /**
     * Pushes the element val onto the stack.
     * 
     * @param val The value to be added.
     */
    public void push(int val) {
        if (head == null) {
            // If stack is empty, the new value is inherently the minimum.
            head = new Node(val, val, null);
        } else {
            // The new minimum is the lesser of the new value and the previous minimum.
            head = new Node(val, Math.min(val, head.min), head);
        }
    }
    
    /**
     * Removes the element on the top of the stack.
     * Operates in O(1) time.
     */
    public void pop() {
        if (head != null) {
            head = head.next;
        }
    }
    
    /**
     * Gets the top element of the stack.
     * 
     * @return The integer at the top of the stack.
     */
    public int top() {
        return head.val;
    }
    
    /**
     * Retrieves the minimum element in the stack.
     * 
     * @return The current minimum integer in the stack.
     */
    public int getMin() {
        return head.min;
    }
}

/**
 * ### Reusable Patterns & Key Takeaways
 * 
 * 1. State Snapshotting: When operations are strictly reversible (like LIFO in a stack), 
 *    you can attach the aggregated state (e.g., the minimum) directly to the elements. 
 *    When you revert the element (pop), you automatically revert to the previous state.
 * 
 * 2. Dynamic vs. Fixed Allocation: Using an array with a `MAX_SIZE` is a common shortcut 
 *    in competitive programming, but it leads to `ArrayIndexOutOfBoundsException` in 
 *    production if limits are exceeded. A Linked List approach organically scales with 
 *    memory without arbitrary boundaries.
 * 
 * 3. Space-Time Tradeoff: We achieve O(1) time complexity for `getMin()` by sacrificing 
 *    O(N) auxiliary space (storing the `min` variable in every node). 
 */