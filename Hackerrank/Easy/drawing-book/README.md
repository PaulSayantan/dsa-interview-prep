# [Drawing Book](https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=false)

## Problem Description
A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book. They always turn pages one at a time. When they open the book, page $1$ is always on the right side.

When they flip page $1$, they see pages $2$ and $3$. Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the book is $n$ pages long, and a student wants to turn to page $p$, what is the minimum number of pages to turn? They can start at the beginning or the end of the book.

Given $n$ and $p$, find and print the minimum number of pages that must be turned in order to arrive at page $p$.

### Constraints
* $1 \le n \le 10^5$
* $1 \le p \le n$

---

## Examples

**Example 1:**
* **Input:** `n = 6`, `p = 2`
* **Output:** `1`
* **Explanation:** Starting from the front, they only need to turn 1 page to see pages 2 and 3. Starting from the back, they would need to turn 2 pages.

**Example 2:**
* **Input:** `n = 5`, `p = 4`
* **Output:** `0`
* **Explanation:** If they start turning from the back of the book (page 5), page 4 is already visible on the left side of the spread. No page turns are needed.

---

## Approach

The problem can be solved in **$O(1)$ time complexity** by taking advantage of integer division. 

Since each physical page turn reveals two numbered pages (an even page on the left, an odd page on the right), we can determine the number of turns from the front of the book simply by dividing the target page number by 2 (`p / 2`). 

To find the turns from the back, we calculate the total possible turns for the entire book (`n / 2`) and subtract the turns it takes to get to our target page (`p / 2`). We then return the minimum of these two values.

### Time and Space Complexity
* **Time Complexity:** $O(1)$ because the answer is calculated using a direct mathematical formula without loops.
* **Space Complexity:** $O(1)$ as we only store a few integer variables.

---