# Leetcode Problem 191: Number of 1 Bits

This is a classic problem in competitive programming and system-level engineering, often serving as a gateway to more advanced bit manipulation techniques. The code snippet you've highlighted is actually a highly optimized approach known as **Brian Kernighan's Algorithm**.

Here is a breakdown to help you master this pattern.

### 1. Conceptual Breakdown

To solve the [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) problem, we need to rely on the fundamentals of how computers represent numbers and how we can alter them at the lowest level:

* **Binary Representation:** Every integer is stored in memory as a sequence of `0`s and `1`s.
* **Hamming Weight:** This is just the formal term for the count of non-zero symbols (in this case, `1`s) in a given sequence.
* **Bitwise AND (`&`):** This operator compares two numbers bit by bit. It returns `1` only if *both* corresponding bits are `1`. Otherwise, it returns `0`.
* Example: `1 & 1 = 1`
* Example: `1 & 0 = 0`



### 2. Intuition Building

The naive way to solve this is to look at all 32 bits of the integer one by one, shifting the bits to the right and checking if the last bit is a `1` using `n & 1`. While that works, it means your loop will always run 32 times, regardless of the number.

The solution you selected is much more elegant because it skips the `0`s entirely. The mental model you should adopt here revolves around this specific question: **What happens to the binary representation of a number when you subtract 1 from it?**

Let's take the number `12`, which is `1100` in binary.
If you subtract `1` to get `11`, the binary becomes `1011`.

Notice the pattern:

1. The rightmost `1` in the original number (`1100`) was flipped to `0`.
2. All the `0`s to the right of it were flipped to `1`s.

Because of this exact flip, if we perform a bitwise AND between the original number and the number minus one—`n & (n - 1)`—we effectively **erase the rightmost `1**` from the original number, leaving the rest of the bits completely untouched.

### 3. Step-by-Step Strategy

To systematically solve this and similar bit-stripping problems, use this blueprint:

1. **Initialize a Tracker:** Set a `count` variable to `0` to keep track of how many `1`s you find.
2. **Establish the Condition:** Use a `while` loop that runs as long as `n` is not `0`. If `n` is `0`, it means there are no more `1` bits left to count.
3. **Apply the Bit Trick:** Inside the loop, execute `n = n & (n - 1)`. This strips exactly one `1` off the number per iteration.
4. **Increment:** For every time the loop runs (meaning a `1` was successfully stripped), increase your `count` by 1.
5. **Return the Result:** Once `n` hits `0`, the loop terminates, and `count` holds the total Hamming weight.

*Performance note:* Because this strategy only loops for the exact number of `1` bits present, its time complexity is $O(k)$ where $k$ is the number of set bits, making it incredibly fast for sparse binary numbers.

### 4. Guided Practice

Let's walk through this together using a small example. We will use **`n = 10`**.
In binary, `10` is represented as **`1010`**.

We start our function.

* Our `count` is `0`.
* Our `n` (`1010`) is not zero, so we enter the `while` loop for our first iteration.

Inside the loop, we are about to execute: `n = n & (n - 1)`
We know `n` is `1010`.
Therefore, `n - 1` (which is 9) is `1001`.

If we perform the bitwise AND operation:
`1010`
`1001`
`----`
Based on the rules of the `&` operator, what is the resulting binary number, and what should our `count` variable be updated to?
