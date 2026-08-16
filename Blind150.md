# 🧠 SDE Algorithmic 150

> **The 150-problem interview grind.**
>
> A pattern-first collection of problems for the algorithms / coding round of an SDE interview.
> The goal isn't to memorize 150 solutions — it's to recognize the pattern, derive the approach, and code it cleanly under pressure.

![Progress](https://img.shields.io/badge/Progress-0%2F150-111827?style=for-the-badge)
![Problems](https://img.shields.io/badge/Problems-150-7c3aed?style=for-the-badge)
![LeetCode](https://img.shields.io/badge/Platform-LeetCode-ffa116?style=for-the-badge&logo=leetcode&logoColor=black)

---

## 🗺️ Roadmap at a Glance

| # | Pattern | Problems | Easy | Medium | Hard |
|---:|---|---:|---:|---:|---:|
| 01 | [🧩 Arrays & Hashing](#arrays-hashing) | **10** | 1 | 9 | 0 |
| 02 | [👉 Two Pointers](#two-pointers) | **7** | 2 | 4 | 1 |
| 03 | [🪟 Sliding Window](#sliding-window) | **9** | 0 | 7 | 2 |
| 04 | [📚 Stack](#stack) | **8** | 0 | 7 | 1 |
| 05 | [🔍 Binary Search](#binary-search) | **8** | 0 | 6 | 2 |
| 06 | [🔗 Linked List](#linked-list) | **10** | 0 | 8 | 2 |
| 07 | [🌳 Trees](#trees) | **14** | 1 | 10 | 3 |
| 08 | [🔤 Tries](#tries) | **4** | 0 | 3 | 1 |
| 09 | [🏔️ Heap / Priority Queue](#heap-priority-queue) | **8** | 0 | 6 | 2 |
| 10 | [🌀 Backtracking](#backtracking) | **8** | 0 | 6 | 2 |
| 11 | [🕸️ Graphs](#graphs) | **14** | 0 | 12 | 2 |
| 12 | [🧠 Advanced Graphs / Union-Find](#advanced-graphs-union-find) | **6** | 0 | 5 | 1 |
| 13 | [🧠 Dynamic Programming (1D)](#dynamic-programming-1d) | **10** | 1 | 9 | 0 |
| 14 | [🧠 Dynamic Programming (2D)](#dynamic-programming-2d) | **8** | 0 | 5 | 3 |
| 15 | [🧠 Greedy & Intervals](#greedy-intervals) | **9** | 0 | 9 | 0 |
| 16 | [🧠 Design](#design) | **8** | 0 | 6 | 2 |
| 17 | [🧠 Math, Bit Manipulation & Geometry](#math-bit-manipulation-geometry) | **6** | 2 | 3 | 1 |
| 18 | [🧠 Matrix](#matrix) | **3** | 0 | 3 | 0 |
| | **TOTAL** | **150** | **7** | **118** | **25** |

### 🎯 Difficulty Mix

- 🟢 **Easy:** 7
- 🟡 **Medium:** 118
- 🔴 **Hard:** 25

---

## 🧭 How to Use This Repo

**Pass 1 — Learn the pattern**
> Solve with notes open. Focus on *why* the pattern works.

**Pass 2 — Solve cold**
> Hide the solution and derive the approach yourself. Give yourself ~30–45 minutes.

**Pass 3 — Interview mode**
> Explain the brute force → optimization → complexity → edge cases out loud.

**Pass 4 — Revisit weak spots**
> Mark the problem again if you needed a hint, couldn't derive the pattern, or wrote a bug-heavy solution.

> 💡 **Rule of thumb:** if you can solve the problem but can't explain *why that pattern was the right choice*, you don't own it yet.

---

## 🧩 01 — Arrays & Hashing

> Hash maps, frequency counting, prefix tricks, in-place array manipulation.

**10 problems** · 🟢 1 · 🟡 9 · 🔴 0

| # | Problem | Difficulty |
|---:|---|---|
| 1 | - [ ] [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | 🟡 Medium |
| 2 | - [ ] [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | 🟡 Medium |
| 3 | - [ ] [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | 🟡 Medium |
| 4 | - [ ] [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | 🟡 Medium |
| 5 | - [ ] [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | 🟡 Medium |
| 6 | - [ ] [3Sum](https://leetcode.com/problems/3sum/) | 🟡 Medium |
| 7 | - [ ] [4Sum](https://leetcode.com/problems/4sum/) | 🟡 Medium |
| 8 | - [ ] [Next Permutation](https://leetcode.com/problems/next-permutation/) | 🟡 Medium |
| 9 | - [ ] [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) | 🟡 Medium |
| 10 | - [ ] [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | 🟢 Easy |

**Pattern checkpoint**

- [ ] I can identify the **Arrays & Hashing** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 👉 02 — Two Pointers

> Use opposing or synchronized pointers to collapse an otherwise quadratic search.

**7 problems** · 🟢 2 · 🟡 4 · 🔴 1

| # | Problem | Difficulty |
|---:|---|---|
| 11 | - [ ] [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 Medium |
| 12 | - [ ] [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | 🔴 Hard |
| 13 | - [ ] [Sort Colors](https://leetcode.com/problems/sort-colors/) | 🟡 Medium |
| 14 | - [ ] [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | 🟡 Medium |
| 15 | - [ ] [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) | 🟡 Medium |
| 16 | - [ ] [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | 🟢 Easy |
| 17 | - [ ] [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | 🟢 Easy |

**Pattern checkpoint**

- [ ] I can identify the **Two Pointers** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🪟 03 — Sliding Window

> Maintain a moving window and update its state incrementally instead of recomputing.

**9 problems** · 🟢 0 · 🟡 7 · 🔴 2

| # | Problem | Difficulty |
|---:|---|---|
| 18 | - [ ] [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟡 Medium |
| 19 | - [ ] [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | 🔴 Hard |
| 20 | - [ ] [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | 🟡 Medium |
| 21 | - [ ] [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | 🟡 Medium |
| 22 | - [ ] [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | 🔴 Hard |
| 23 | - [ ] [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | 🟡 Medium |
| 24 | - [ ] [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | 🟡 Medium |
| 25 | - [ ] [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | 🟡 Medium |
| 26 | - [ ] [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | 🟡 Medium |

**Pattern checkpoint**

- [ ] I can identify the **Sliding Window** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 📚 04 — Stack

> Think LIFO, monotonic stacks, matching delimiters, and next-greater/smaller relationships.

**8 problems** · 🟢 0 · 🟡 7 · 🔴 1

| # | Problem | Difficulty |
|---:|---|---|
| 27 | - [ ] [Min Stack](https://leetcode.com/problems/min-stack/) | 🟡 Medium |
| 28 | - [ ] [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | 🟡 Medium |
| 29 | - [ ] [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | 🔴 Hard |
| 30 | - [ ] [Decode String](https://leetcode.com/problems/decode-string/) | 🟡 Medium |
| 31 | - [ ] [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | 🟡 Medium |
| 32 | - [ ] [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | 🟡 Medium |
| 33 | - [ ] [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | 🟡 Medium |
| 34 | - [ ] [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | 🟡 Medium |

**Pattern checkpoint**

- [ ] I can identify the **Stack** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🔍 05 — Binary Search

> Look for a sorted search space or a monotonic yes/no condition.

**8 problems** · 🟢 0 · 🟡 6 · 🔴 2

| # | Problem | Difficulty |
|---:|---|---|
| 35 | - [ ] [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | 🟡 Medium |
| 36 | - [ ] [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | 🟡 Medium |
| 37 | - [ ] [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | 🟡 Medium |
| 38 | - [ ] [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 Hard |
| 39 | - [ ] [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | 🟡 Medium |
| 40 | - [ ] [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | 🟡 Medium |
| 41 | - [ ] [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | 🟡 Medium |
| 42 | - [ ] [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | 🔴 Hard |

**Pattern checkpoint**

- [ ] I can identify the **Binary Search** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🔗 06 — Linked List

> Pointer rewiring, fast/slow pointers, dummy nodes, and cycle detection.

**10 problems** · 🟢 0 · 🟡 8 · 🔴 2

| # | Problem | Difficulty |
|---:|---|---|
| 43 | - [ ] [Reorder List](https://leetcode.com/problems/reorder-list/) | 🟡 Medium |
| 44 | - [ ] [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | 🟡 Medium |
| 45 | - [ ] [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | 🟡 Medium |
| 46 | - [ ] [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | 🔴 Hard |
| 47 | - [ ] [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | 🔴 Hard |
| 48 | - [ ] [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | 🟡 Medium |
| 49 | - [ ] [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | 🟡 Medium |
| 50 | - [ ] [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) | 🟡 Medium |
| 51 | - [ ] [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) | 🟡 Medium |
| 52 | - [ ] [Sort List](https://leetcode.com/problems/sort-list/) | 🟡 Medium |

**Pattern checkpoint**

- [ ] I can identify the **Linked List** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🌳 07 — Trees

> DFS/BFS, recursion, BST invariants, tree construction, and path-based state.

**14 problems** · 🟢 1 · 🟡 10 · 🔴 3

| # | Problem | Difficulty |
|---:|---|---|
| 53 | - [ ] [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | 🟡 Medium |
| 54 | - [ ] [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | 🟡 Medium |
| 55 | - [ ] [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | 🔴 Hard |
| 56 | - [ ] [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | 🟡 Medium |
| 57 | - [ ] [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | 🟡 Medium |
| 58 | - [ ] [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | 🔴 Hard |
| 59 | - [ ] [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | 🟡 Medium |
| 60 | - [ ] [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | 🟡 Medium |
| 61 | - [ ] [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | 🟡 Medium |
| 62 | - [ ] [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | 🟢 Easy |
| 63 | - [ ] [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | 🔴 Hard |
| 64 | - [ ] [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | 🟡 Medium |
| 65 | - [ ] [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | 🟡 Medium |
| 66 | - [ ] [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | 🟡 Medium |

**Pattern checkpoint**

- [ ] I can identify the **Trees** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🔤 08 — Tries

> Prefix-based lookup where each character becomes a node in a compact search tree.

**4 problems** · 🟢 0 · 🟡 3 · 🔴 1

| # | Problem | Difficulty |
|---:|---|---|
| 67 | - [ ] [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | 🟡 Medium |
| 68 | - [ ] [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | 🟡 Medium |
| 69 | - [ ] [Word Search II](https://leetcode.com/problems/word-search-ii/) | 🔴 Hard |
| 70 | - [ ] [Replace Words](https://leetcode.com/problems/replace-words/) | 🟡 Medium |

**Pattern checkpoint**

- [ ] I can identify the **Tries** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🏔️ 09 — Heap / Priority Queue

> Repeatedly extract the current min/max or maintain the top-k frontier.

**8 problems** · 🟢 0 · 🟡 6 · 🔴 2

| # | Problem | Difficulty |
|---:|---|---|
| 71 | - [ ] [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟡 Medium |
| 72 | - [ ] [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | 🔴 Hard |
| 73 | - [ ] [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | 🟡 Medium |
| 74 | - [ ] [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | 🟡 Medium |
| 75 | - [ ] [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | 🔴 Hard |
| 76 | - [ ] [Reorganize String](https://leetcode.com/problems/reorganize-string/) | 🟡 Medium |
| 77 | - [ ] [Minimum Platforms](https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1) | 🟡 Medium |
| 78 | - [ ] [Design Twitter](https://leetcode.com/problems/design-twitter/) | 🟡 Medium |

**Pattern checkpoint**

- [ ] I can identify the **Heap / Priority Queue** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🌀 10 — Backtracking

> Explore a decision tree, prune invalid branches, then undo the choice.

**8 problems** · 🟢 0 · 🟡 6 · 🔴 2

| # | Problem | Difficulty |
|---:|---|---|
| 79 | - [ ] [Word Search](https://leetcode.com/problems/word-search/) | 🟡 Medium |
| 80 | - [ ] [Combination Sum](https://leetcode.com/problems/combination-sum/) | 🟡 Medium |
| 81 | - [ ] [Permutations II](https://leetcode.com/problems/permutations-ii/) | 🟡 Medium |
| 82 | - [ ] [Subsets II](https://leetcode.com/problems/subsets-ii/) | 🟡 Medium |
| 83 | - [ ] [N-Queens](https://leetcode.com/problems/n-queens/) | 🔴 Hard |
| 84 | - [ ] [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | 🟡 Medium |
| 85 | - [ ] [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | 🟡 Medium |
| 86 | - [ ] [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | 🔴 Hard |

**Pattern checkpoint**

- [ ] I can identify the **Backtracking** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🕸️ 11 — Graphs

> Model relationships explicitly; master BFS, DFS, topological order, DSU, and shortest paths.

**14 problems** · 🟢 0 · 🟡 12 · 🔴 2

| # | Problem | Difficulty |
|---:|---|---|
| 87 | - [ ] [Number of Islands](https://leetcode.com/problems/number-of-islands/) | 🟡 Medium |
| 88 | - [ ] [Clone Graph](https://leetcode.com/problems/clone-graph/) | 🟡 Medium |
| 89 | - [ ] [Course Schedule](https://leetcode.com/problems/course-schedule/) | 🟡 Medium |
| 90 | - [ ] [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 🟡 Medium |
| 91 | - [ ] [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | 🟡 Medium |
| 92 | - [ ] [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | 🟡 Medium |
| 93 | - [ ] [Word Ladder](https://leetcode.com/problems/word-ladder/) | 🔴 Hard |
| 94 | - [ ] [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | 🟡 Medium |
| 95 | - [ ] [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | 🟡 Medium |
| 96 | - [ ] [01 Matrix](https://leetcode.com/problems/01-matrix/) | 🟡 Medium |
| 97 | - [ ] [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | 🟡 Medium |
| 98 | - [ ] [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | 🟡 Medium |
| 99 | - [ ] [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | 🟡 Medium |
| 100 | - [ ] [Minimum Number of Days to Disconnect Island](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/) | 🔴 Hard |

**Pattern checkpoint**

- [ ] I can identify the **Graphs** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🧠 12 — Advanced Graphs / Union-Find

> Recognize the core invariant, choose the right data structure, and optimize the search space.

**6 problems** · 🟢 0 · 🟡 5 · 🔴 1

| # | Problem | Difficulty |
|---:|---|---|
| 101 | - [ ] [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | 🟡 Medium |
| 102 | - [ ] [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | 🟡 Medium |
| 103 | - [ ] [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | 🟡 Medium |
| 104 | - [ ] [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | 🔴 Hard |
| 105 | - [ ] [Alien Dictionary](https://www.geeksforgeeks.org/problems/alien-dictionary/1) | 🟡 Medium |
| 106 | - [ ] [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | 🟡 Medium |

**Pattern checkpoint**

- [ ] I can identify the **Advanced Graphs / Union-Find** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🧠 13 — Dynamic Programming (1D)

> Recognize the core invariant, choose the right data structure, and optimize the search space.

**10 problems** · 🟢 1 · 🟡 9 · 🔴 0

| # | Problem | Difficulty |
|---:|---|---|
| 107 | - [ ] [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | 🟢 Easy |
| 108 | - [ ] [House Robber II](https://leetcode.com/problems/house-robber-ii/) | 🟡 Medium |
| 109 | - [ ] [Decode Ways](https://leetcode.com/problems/decode-ways/) | 🟡 Medium |
| 110 | - [ ] [Coin Change](https://leetcode.com/problems/coin-change/) | 🟡 Medium |
| 111 | - [ ] [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | 🟡 Medium |
| 112 | - [ ] [Word Break](https://leetcode.com/problems/word-break/) | 🟡 Medium |
| 113 | - [ ] [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | 🟡 Medium |
| 114 | - [ ] [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | 🟡 Medium |
| 115 | - [ ] [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | 🟡 Medium |
| 116 | - [ ] [Perfect Squares](https://leetcode.com/problems/perfect-squares/) | 🟡 Medium |

**Pattern checkpoint**

- [ ] I can identify the **Dynamic Programming (1D)** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🧠 14 — Dynamic Programming (2D)

> Recognize the core invariant, choose the right data structure, and optimize the search space.

**8 problems** · 🟢 0 · 🟡 5 · 🔴 3

| # | Problem | Difficulty |
|---:|---|---|
| 117 | - [ ] [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | 🟡 Medium |
| 118 | - [ ] [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | 🟡 Medium |
| 119 | - [ ] [Edit Distance](https://leetcode.com/problems/edit-distance/) | 🔴 Hard |
| 120 | - [ ] [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 🟡 Medium |
| 121 | - [ ] [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | 🟡 Medium |
| 122 | - [ ] [Interleaving String](https://leetcode.com/problems/interleaving-string/) | 🟡 Medium |
| 123 | - [ ] [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | 🔴 Hard |
| 124 | - [ ] [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | 🔴 Hard |

**Pattern checkpoint**

- [ ] I can identify the **Dynamic Programming (2D)** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🧠 15 — Greedy & Intervals

> Recognize the core invariant, choose the right data structure, and optimize the search space.

**9 problems** · 🟢 0 · 🟡 9 · 🔴 0

| # | Problem | Difficulty |
|---:|---|---|
| 125 | - [ ] [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | 🟡 Medium |
| 126 | - [ ] [Insert Interval](https://leetcode.com/problems/insert-interval/) | 🟡 Medium |
| 127 | - [ ] [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | 🟡 Medium |
| 128 | - [ ] [Car Pooling](https://leetcode.com/problems/car-pooling/) | 🟡 Medium |
| 129 | - [ ] [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | 🟡 Medium |
| 130 | - [ ] [Gas Station](https://leetcode.com/problems/gas-station/) | 🟡 Medium |
| 131 | - [ ] [Partition Labels](https://leetcode.com/problems/partition-labels/) | 🟡 Medium |
| 132 | - [ ] [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | 🟡 Medium |
| 133 | - [ ] [My Calendar I](https://leetcode.com/problems/my-calendar-i/) | 🟡 Medium |

**Pattern checkpoint**

- [ ] I can identify the **Greedy & Intervals** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🧠 16 — Design

> Recognize the core invariant, choose the right data structure, and optimize the search space.

**8 problems** · 🟢 0 · 🟡 6 · 🔴 2

| # | Problem | Difficulty |
|---:|---|---|
| 134 | - [ ] [LRU Cache](https://leetcode.com/problems/lru-cache/) | 🟡 Medium |
| 135 | - [ ] [LFU Cache](https://leetcode.com/problems/lfu-cache/) | 🔴 Hard |
| 136 | - [ ] [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | 🟡 Medium |
| 137 | - [ ] [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) | 🟡 Medium |
| 138 | - [ ] [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | 🟡 Medium |
| 139 | - [ ] [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | 🟡 Medium |
| 140 | - [ ] [All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/) | 🔴 Hard |
| 141 | - [ ] [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | 🟡 Medium |

**Pattern checkpoint**

- [ ] I can identify the **Design** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🧠 17 — Math, Bit Manipulation & Geometry

> Recognize the core invariant, choose the right data structure, and optimize the search space.

**6 problems** · 🟢 2 · 🟡 3 · 🔴 1

| # | Problem | Difficulty |
|---:|---|---|
| 142 | - [ ] [Single Number II](https://leetcode.com/problems/single-number-ii/) | 🟡 Medium |
| 143 | - [ ] [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | 🟡 Medium |
| 144 | - [ ] [Counting Bits](https://leetcode.com/problems/counting-bits/) | 🟢 Easy |
| 145 | - [ ] [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | 🟢 Easy |
| 146 | - [ ] [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) | 🔴 Hard |
| 147 | - [ ] [Pow(x, n)](https://leetcode.com/problems/powx-n/) | 🟡 Medium |

**Pattern checkpoint**

- [ ] I can identify the **Math, Bit Manipulation & Geometry** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 🧠 18 — Matrix

> Recognize the core invariant, choose the right data structure, and optimize the search space.

**3 problems** · 🟢 0 · 🟡 3 · 🔴 0

| # | Problem | Difficulty |
|---:|---|---|
| 148 | - [ ] [Rotate Image](https://leetcode.com/problems/rotate-image/) | 🟡 Medium |
| 149 | - [ ] [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | 🟡 Medium |
| 150 | - [ ] [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | 🟡 Medium |

**Pattern checkpoint**

- [ ] I can identify the **Matrix** pattern without a hint.
- [ ] I can explain the optimal approach before coding.
- [ ] I can state time + space complexity.
- [ ] I can handle edge cases without trial-and-error.

---

## 📊 Progress Tracker

Update the counters as you go:

```text
Solved       0 / 150
Revisited    0 / 150
Mastered     0 / 150

[░░░░░░░░░░░░░░░░░░░░] 0%
```

### 🏁 Readiness Check

- [ ] I can solve most Easy problems without help.
- [ ] I can solve most Medium problems within 30–45 minutes.
- [ ] I recognize common patterns before writing code.
- [ ] I can derive a brute-force solution first, then optimize it.
- [ ] I can communicate trade-offs clearly while coding.
- [ ] I have revisited every problem I previously missed.

---

## 🧠 The Real Goal

```text
150 problems
      ↓
~15 core patterns
      ↓
Pattern recognition
      ↓
Fast problem decomposition
      ↓
Clean interview-ready solutions
```

> **Don't memorize the answer. Memorize the signal that tells you which pattern to use.**

### ⚔️ Interview mantra

`Understand → Clarify → Brute Force → Optimize → Prove → Code → Test`

---

## ⭐ Credits

Problem links point to **LeetCode**. Difficulty and categorization are based on the supplied problem list.

**Built for the grind. Stay curious. Ship the solution.**
