#include <string>
#include <stack>

class Solution {
public:
    /**
     * Determines if the input string of brackets is valid without a map template.
     * * INTUITION:
     * Utilizing sequential `if-else` branches to place anticipated closing brackets 
     * onto the stack maximizes runtime efficiency in compiled environments by 
     * avoiding hashing computations.
     * * COMPLEXITY ANALYSIS:
     * - Time Complexity: O(n)
     * - Space Complexity: O(n)
     */
    bool isValid(std::string s) {
        // Early exit optimization
        if (s.length() % 2 != 0) {
            return false;
        }

        std::stack<char> bracket_stack;

        for (char ch : s) {
            if (ch == '(') {
                bracket_stack.push(')');
            } else if (ch == '{') {
                bracket_stack.push('}');
            } else if (ch == '[') {
                bracket_stack.push(']');
            } 
            else {
                if (bracket_stack.empty() || bracket_stack.top() != ch) {
                    return false;
                }
                bracket_stack.pop();
            }
        }

        return bracket_stack.empty();
    }
};