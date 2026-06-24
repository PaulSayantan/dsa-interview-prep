/*
longestPalindrome finds the longest palindromic substring in a given string.

METHODOLOGY: Expand Around Center
Instead of checking every possible substring, we iterate through each character 
in the string and treat it as the center of a potential palindrome. We then 
expand outward.

TIME COMPLEXITY: O(n^2)
- We visit each character in the string of length n: O(n)
- For each character, the expansion loop can run up to n times: O(n)
- Total time = O(n) * O(n) = O(n^2)

SPACE COMPLEXITY: O(1)
- We only store integer variables for indices and maximum lengths. No additional 
  dynamic programming arrays are allocated.
*/
func longestPalindrome(s string) string {
    // Edge case: If the string is empty, return an empty string.
    if len(s) == 0 {
        return ""
    }

    // These will track the absolute start and end indices of the longest palindrome.
    start, end := 0, 0

    // Iterate through every character to treat it as a center.
    for i := 0; i < len(s); i++ {
        // Case 1: Odd length palindromes (e.g., "aba")
        // The center is exactly at index i.
        len1 := expandAroundCenter(s, i, i)
        
        // Case 2: Even length palindromes (e.g., "abba")
        // The center is strictly between index i and i+1.
        len2 := expandAroundCenter(s, i, i+1)
        
        // Find the maximum length between the odd and even cases
        maxLen := len1
        if len2 > len1 {
            maxLen = len2
        }
        
        // If the newly found palindrome is longer than our current record,
        // update the start and end boundary indices.
        if maxLen > end - start {
            start = i - (maxLen - 1) / 2
            end = i + maxLen / 2
        }
    }

    // Go string slicing is inclusive for the start index and exclusive for the end index.
    return s[start : end+1]
}

/*
expandAroundCenter acts as a helper to expand outward from a given center.

:param s: The original string.
:param left: The starting left index of the center.
:param right: The starting right index of the center.
:return: The total integer length of the valid palindrome.
*/
func expandAroundCenter(s string, left int, right int) int {
    // Continue expanding outward as long as:
    // 1. We stay within the string boundaries.
    // 2. The characters at the left and right pointers match.
    for left >= 0 && right < len(s) && s[left] == s[right] {
        left--
        right++
    }
    
    // Once the loop breaks, s[left] != s[right]. 
    // The actual distance/length between the valid pointers is (right - left - 1).
    return right - left - 1
}

/*
================================================================================
REUSABLE PATTERNS & KEY TAKEAWAYS
================================================================================

1. OPTIMIZING MEMORY IN GO:
   - In Python, it's common to pass substrings around. In Go, it's significantly 
     faster to pass around integer indices (pointers) and calculate lengths.
   - Wait to slice the string until the absolute end to minimize allocations 
     and keep space complexity at O(1).

2. THE INDEX MATH PATTERN:
   - When expanding around a center `i`, calculating the bounds based on the length can be tricky. 
   - Start index = i - (length - 1) / 2
   - End index   = i + length / 2
   - Memorize this calculation pattern; it perfectly resolves the math differences between odd-length and even-length expansions.

3. GO'S LACK OF A BUILT-IN MAX() FOR INTS:
   - Unlike Python, Go (prior to 1.21) doesn't have a simple `math.Max` for `int` (it only takes `float64`). 
   You will often write a quick `if a > b { max = a }` block. 
   
   (Note: Go 1.21+ introduced a built-in `max` function, but writing out the conditional is still universally backwards-compatible).
================================================================================
*/