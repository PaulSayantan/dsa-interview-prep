# Leetcode Problem 125: Valid palindrome

### 1. Conceptual Breakdown

To solve this problem, we need to understand a few core concepts:

* **Palindrome:** A sequence of characters that reads the same forwards and backwards (e.g., "radar" or "level").
* **Alphanumeric Filtering:** The problem strictly specifies that we only care about letters (a-z, A-Z) and numbers (0-9). Spaces, commas, and punctuation must be entirely ignored.
* **Case Insensitivity:** 'A' and 'a' are treated as the exact same character.
* **The Two-Pointer Technique:** This is a fundamental algorithmic pattern where two reference points (variables storing array/string indices) move through a data structure simultaneously to compare elements.

### 2. Intuition Building

**The "Why" behind the optimal solution:**

A naive approach to this problem is to create a brand new, "cleaned" version of the string (removing all spaces and punctuation, and converting to lowercase), and then comparing that new string to its reverse. While this works, it requires $O(N)$ extra space to build and store the new strings.

*How can we do this without using extra memory?*

Imagine you and a friend are standing at opposite ends of a long line of painted letters on the ground. You both step toward each other. If one of you steps on a blank space or a punctuation mark, you just take another step forward until you are on a valid letter. Once you are both standing on letters, you shout them out. If they match, you both take another step inward. If they don't, you immediately know the line isn't a palindrome.

This mental model represents the **In-Place Two-Pointer approach**. It allows us to verify the palindrome by just "looking" at the characters without building a whole new string, optimizing our space complexity to $O(1)$.

### 3. Step-by-Step Strategy

When facing a Two-Pointer string comparison problem, use this repeatable process:

1. **Initialize Pointers:** Create a `left` pointer starting at index `0` and a `right` pointer starting at the last index (`length - 1`).
2. **Start the Traversal:** Use a `while` loop that continues as long as `left < right`. (If they cross, you've checked the whole string).
3. **Skip Invalid Characters (Left):** Inside the loop, if the character at `left` is not alphanumeric, move `left` forward (`left += 1`).
4. **Skip Invalid Characters (Right):** Similarly, if the character at `right` is not alphanumeric, move `right` backward (`right -= 1`).
5. **Compare Valid Characters:** Once both pointers are resting on alphanumeric characters, convert them to the same case (e.g., lowercase) and compare them.
* If they do **not** match, stop immediately and return `False`.
* If they **do** match, step both pointers inward (`left += 1`, `right -= 1`) to check the next pair.


6. **Conclude:** If the loop naturally finishes without ever finding a mismatch, the string is a palindrome. Return `True`.



Both of these initial characters are alphanumeric, so we don't need to skip anything yet. We are ready for our first comparison.

Before we move the pointers inward, what exactly does our code need to do to these two specific characters ('R' and 'r') so that they successfully match?
