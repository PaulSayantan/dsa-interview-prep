import java.util.Stack;

class Solution {
    /**
     * Determines if the input string of brackets is valid without a HashMap.
     * * INTUITION:
     * By matching opening characters manually and pushing their respective closing
     * counterparts to the Stack, we eliminate the memory overhead and lookup cost 
     * of a traditional map.
     * * COMPLEXITY ANALYSIS:
     * - Time Complexity: O(n) where n is the length of the string.
     * - Space Complexity: O(n) worst-case memory consumption for the stack.
     */
    public boolean isValid(String s) {
        // Early exit optimization: Valid pairs require an even string length
        if (s.length() % 2 != 0) {
            return false;
        }

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            // Push the expected closing bracket directly
            if (ch == '(') {
                stack.push(')');
            } else if (ch == '{') {
                stack.push('}');
            } else if (ch == '[') {
                stack.push(']');
            } 
            // Validate closing bracket structure
            else {
                if (stack.isEmpty() || stack.pop() != ch) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}