# LeetCode 3691 · Maximum Total Subarray Value II

---

## Problem Statement

> Given an integer array `nums` of length `n` and an integer `k`, select **exactly `k` distinct,
> non-empty subarrays** `nums[l..r]`.  
> Subarrays **may overlap**, but the **exact same** `(l, r)` pair cannot be chosen more than once.  
>
> The **value** of a subarray `nums[l..r]` is:
> ```
> value(l, r) = max(nums[l..r]) − min(nums[l..r])
> ```
> Return the **maximum possible total value** (sum of values of all chosen subarrays).

### Constraints

| Symbol | Bound |
|--------|-------|
| `n` | 1 ≤ n ≤ 5 × 10⁴ |
| `nums[i]` | 0 ≤ nums[i] ≤ 10⁹ |
| `k` | 1 ≤ k ≤ min(10⁵, n(n+1)/2) |

### Official Examples

**Example 1**
```
nums = [1, 3, 2],  k = 2
```
Pick `[0..1]` → value 2, and `[0..2]` → value 2. Total = **4**.

**Example 2**
```
nums = [4, 2, 5, 1],  k = 3
```
Pick `[0..3]`, `[1..3]`, `[2..3]` → all have value 4. Total = **12**.

---

## Part I vs Part II — The Critical Difference

| | Part I | Part II |
|---|---|---|
| Repeat same subarray? | ✅ Allowed | ❌ Not allowed |
| Strategy | Multiply global max value × k | Find the top-k **distinct** subarray values |
| Difficulty | Easy | Hard |

In **Part I** you greedily take the globally best subarray k times. In **Part II** that shortcut is
gone. You must find the **k largest values** across all n(n+1)/2 distinct subarrays — which can be
up to ~1.25 × 10⁹ subarrays for the given constraints, so brute force is completely off the table.

---

## Why Brute Force Fails

| Approach | Time | Verdict |
|----------|------|---------|
| Enumerate all subarrays + scan for max/min | O(n³) | TLE |
| Enumerate all subarrays + precomputed prefix | O(n²) | TLE / MLE for n = 5×10⁴ |
| This solution (Sparse Table + Heap) | O((n + k) log n) | ✅ Accepted |

---

## Key Insight 1 — Monotonicity of `value(l, r)` over `r`

**Fix the left endpoint `l` and expand `r` to the right.**

As `r` grows:
- `max(nums[l..r])` is **non-decreasing** — a new element can only raise or keep the maximum.
- `min(nums[l..r])` is **non-increasing** — a new element can only lower or keep the minimum.

Therefore `value(l, r) = max − min` is **monotonically non-decreasing** in `r`.

```
For l = 0, nums = [1, 3, 2, 5]:
  r=0  → [1]         → value 0
  r=1  → [1,3]       → value 2   (max went up)
  r=2  → [1,3,2]     → value 2   (unchanged)
  r=3  → [1,3,2,5]   → value 4   (max went up again)
  Sequence: 0 ≤ 2 ≤ 2 ≤ 4  ✓ non-decreasing
```

**Consequence:** For every fixed `l`, the **largest possible value** starting at `l` is always the
full-length interval `(l, n-1)`. The values form a sorted list from left to right.

> ⚠️ The same monotonicity does **NOT** hold if you fix `r` and shrink from the left —  
> value can both rise and fall when `l` moves. Fixing `l` and moving `r` is the correct framing.

---

## Key Insight 2 — Reduction to "Top-K from N Sorted Lists"

Because each row (fixed `l`) is a sorted list of values:

```
l=0 : 0  2  2  4       (r = 0,1,2,3)
l=1 : 0  1  3          (r = 1,2,3)
l=2 : 0  3             (r = 2,3)
l=3 : 0                (r = 3)
```

**We need the k largest numbers drawn from these n sorted lists** — a classic heap problem.

The standard algorithm is:
1. Seed the heap with the **maximum** of each list (i.e., the rightmost element of each row).
2. Pop the globally largest element; then push the **next** element from the same list (one step left).
3. Repeat k times.

This guarantees we always extract the next globally largest value in O(log n) time.

---

## Key Insight 3 — O(1) Range Queries via Sparse Table

Computing `value(l, r)` naively by scanning takes O(n) per query. With O(k) heap pops each
potentially triggering a fresh query, naive scanning would cost O(nk) — too slow.

**Sparse Tables** solve this. Because the array is static (no updates needed), we can precompute
range-max and range-min in O(n log n) time and answer any `[l, r]` query in **O(1)**.

### How a Sparse Table Works

A sparse table stores answers for all intervals whose **length is a power of two**.

```
st[i][j]  =  answer for the interval  [i,  i + 2^j − 1]
```

**Build rule (bottom-up):**
```
st[i][0] = nums[i]                          # length-1 base case
st[i][j] = combine(st[i][j-1],             # left half
                   st[i + 2^(j-1)][j-1])   # right half
```

**Query `[l, r]`:**  
Find the largest power of two that fits in the interval: `p = floor(log2(r - l + 1))`.  
Cover `[l, r]` with **two overlapping blocks of length 2^p** — the overlap is harmless for max/min:

```
answer = combine(st[l][p],  st[r - 2^p + 1][p])
```

This works because max and min are **idempotent** — repeated elements don't affect the result.

```
Query [1, 3] on [1, 3, 2, 5]:
  length = 3,  p = floor(log2(3)) = 1  →  block size = 2
  Block A: [1, 2]  →  st_max[1][1] = max(3,2) = 3
  Block B: [2, 3]  →  st_max[2][1] = max(2,5) = 5
  max(3, 5) = 5  ✓
```

> **Why not a segment tree?** Segment trees also give O(log n) queries, but sparse tables give O(1)
> with smaller constants. Since the array never changes, the O(n log n) build cost is paid once and
> the O(1) query benefit compounds across all k + n heap operations.

---

## Algorithm Walkthrough

### Step 1 — Build Two Sparse Tables

One for range-max, one for range-min. Both use the same structure.

```python
LOG = n.bit_length()          # ceil(log2(n)) + 1; safe upper bound

st_max[i][0] = nums[i]        # base case for all i
st_min[i][0] = nums[i]

for each power j = 1, 2, ...:
    for each valid starting index i:
        st_max[i][j] = max(st_max[i][j-1], st_max[i + 2^(j-1)][j-1])
        st_min[i][j] = min(st_min[i][j-1], st_min[i + 2^(j-1)][j-1])
```

### Step 2 — O(1) Value Query

```python
def get_value(l, r):
    length = r - l + 1
    p = length.bit_length() - 1          # floor(log2(length))
    mx = max(st_max[l][p], st_max[r - (1<<p) + 1][p])
    mn = min(st_min[l][p], st_min[r - (1<<p) + 1][p])
    return mx - mn
```

### Step 3 — Seed the Max Heap

For every left endpoint `l`, push the best possible interval `(l, n-1)`:

```python
for l in range(n):
    heappush(heap, (-get_value(l, n-1), l, n-1))
```

Python's `heapq` is a **min-heap**, so we negate values to simulate a max-heap.

### Step 4 — Extract Top-K

```python
answer = 0
for _ in range(k):
    neg_val, l, r = heappop(heap)
    answer += -neg_val
    if r > l:                            # list not exhausted
        heappush(heap, (-get_value(l, r-1), l, r-1))
return answer
```

After popping `(l, r)`, the next best candidate from row `l` is `(l, r-1)` — one step left in the
sorted row.

---

## Full Dry Run

```
nums = [1, 3, 2],  k = 2
```

**Value table (all distinct subarrays):**

| (l, r) | Subarray | value |
|--------|----------|-------|
| (0,0) | [1] | 0 |
| (0,1) | [1,3] | 2 |
| (0,2) | [1,3,2] | 2 |
| (1,1) | [3] | 0 |
| (1,2) | [3,2] | 1 |
| (2,2) | [2] | 0 |

**Rows (sorted by r, left to right = increasing value):**
```
l=0: 0  2  2      ← best is (0,2) with value 2
l=1: 0  1         ← best is (1,2) with value 1
l=2: 0            ← best is (2,2) with value 0
```

**Initial heap** (max-heap, shown as positives):
```
[ (2, l=0, r=2),  (1, l=1, r=2),  (0, l=2, r=2) ]
```

**Iteration 1** — pop `(2, l=0, r=2)`:
```
answer = 2
Push next from row 0: (l=0, r=1) → value 2
Heap: [ (2, l=0, r=1),  (1, l=1, r=2),  (0, l=2, r=2) ]
```

**Iteration 2** — pop `(2, l=0, r=1)`:
```
answer = 2 + 2 = 4
r=1 > l=0, so push (l=0, r=0) → value 0  (but we're done)
```

**Final answer: 4** ✓

---

## Full Python Implementation (Annotated)

```python
from heapq import heappush, heappop

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:

        n = len(nums)

        # ── Sparse Table Construction ────────────────────────────────────
        # LOG levels are enough to cover any interval of length ≤ n
        LOG = n.bit_length()

        st_max = [[0] * LOG for _ in range(n)]
        st_min = [[0] * LOG for _ in range(n)]

        # Level 0: interval of length 1
        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]

        # Level j: combine two non-overlapping halves of length 2^(j-1)
        j = 1
        while (1 << j) <= n:
            half = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j-1], st_max[i + half][j-1])
                st_min[i][j] = min(st_min[i][j-1], st_min[i + half][j-1])
            j += 1

        # ── O(1) Range Query ─────────────────────────────────────────────
        def get_value(l: int, r: int) -> int:
            p = (r - l + 1).bit_length() - 1   # floor(log2(length))
            overlap = r - (1 << p) + 1          # start of right block
            mx = max(st_max[l][p], st_max[overlap][p])
            mn = min(st_min[l][p], st_min[overlap][p])
            return mx - mn

        # ── Seed Heap ────────────────────────────────────────────────────
        # Each left endpoint l contributes a sorted sequence of values.
        # Its global best is always the full-length interval (l, n-1).
        heap = []
        for l in range(n):
            val = get_value(l, n - 1)
            heappush(heap, (-val, l, n - 1))   # negate → max-heap

        # ── Extract Top-K ────────────────────────────────────────────────
        answer = 0
        for _ in range(k):
            neg_val, l, r = heappop(heap)
            answer += -neg_val

            # The next best interval for left endpoint l is (l, r-1)
            if r > l:
                heappush(heap, (-get_value(l, r - 1), l, r - 1))

        return answer
```

---

## Correctness Proof (Informal)

**Claim:** At every heap-pop, we extract the globally largest remaining subarray value.

**Argument:**

1. Each "row" `l` is a sorted list `v(l,l) ≤ v(l,l+1) ≤ … ≤ v(l,n-1)`.
2. The heap always holds exactly one pointer into each row — the **current maximum** of that row.
3. The globally largest unused value must be the maximum across all rows' current pointers — which is exactly what a max-heap returns.
4. After consuming `v(l, r)`, the next largest from row `l` is `v(l, r-1)`, so we push that back.

By induction, every pop produces the next globally largest value. Summing k pops gives the maximum possible total.

---

## Complexity Summary

| Phase | Time | Space |
|-------|------|-------|
| Sparse table build | O(n log n) | O(n log n) |
| Heap seed (n pushes) | O(n log n) | O(n) |
| k heap operations | O(k log n) | O(1) amortised |
| **Total** | **O((n + k) log n)** | **O(n log n)** |

For the given constraints (n ≤ 5×10⁴, k ≤ 10⁵) this is comfortably within time limits.

---

## Edge Cases to Consider

| Scenario | Behaviour |
|----------|-----------|
| All elements equal | Every subarray has value 0; answer = 0 |
| k = 1 | Just pop the heap once (the globally largest interval) |
| k = n(n+1)/2 | All subarrays are selected; heap drains completely |
| n = 1 | Only one subarray `[0,0]` with value 0; heap has one entry |
| Strictly increasing array | Each `v(l, n-1)` grows as l decreases; answer comes from long intervals |

---

## Common Mistakes and Pitfalls

| Mistake | Why it's wrong | Fix |
|---------|---------------|-----|
| Using `r = 0` as the start | Row is sorted ascending; you must start from `r = n-1` | Always seed with `(l, n-1)` |
| Fixing `r` and shrinking `l` | The monotonicity argument only holds for fixed `l`, expanding `r` | Always fix `l`, vary `r` |
| Using `math.log2` for `p` | Floating-point rounding errors (e.g. `log2(4)` could give `1.9999…`) | Use `(length).bit_length() - 1` |
| Forgetting `r > l` guard | Pushing `(l, l-1)` is invalid | Check `r > l` before pushing |
| Using min-heap directly | Python's `heapq` is a min-heap | Negate values for max-heap simulation |

---

## Pattern Recognition Cheat Sheet

When you see a problem matching these signals, this pattern applies:

| Signal | Interpretation |
|--------|---------------|
| "Top k subarrays" | Top-K from N sorted lists + heap |
| "Subarray value = range max − range min" | Fixing one endpoint creates monotone sequence |
| "Static array, range queries" | Sparse table for O(1) queries |
| "n up to 5×10⁴, k up to 10⁵" | O((n+k) log n) is the target complexity |

**Template to recognize:**
> _Fix one endpoint → monotone sequence → sorted list → heap merge of N sorted lists_

Other problems using the same core idea:
- **Kth Largest Sum in a Binary Tree** (heap + sorted path values)
- **Find K Pairs with Smallest Sums** (heap over two sorted arrays)
- **K-th Smallest Element in a Sorted Matrix** (heap over sorted rows/columns)

---

## Quick Reference — `bit_length()` vs `math.log2()`

Python's `int.bit_length()` returns the number of bits needed to represent an integer:
```
(1).bit_length()  = 1   →   floor(log2(1)) = 0   →   p = 0
(2).bit_length()  = 2   →   floor(log2(2)) = 1   →   p = 1
(3).bit_length()  = 2   →   floor(log2(3)) = 1   →   p = 1
(4).bit_length()  = 3   →   floor(log2(4)) = 2   →   p = 2
(7).bit_length()  = 3   →   floor(log2(7)) = 2   →   p = 2
(8).bit_length()  = 4   →   floor(log2(8)) = 3   →   p = 3
```

So `floor(log2(x)) = x.bit_length() - 1`. This is faster and exact — always prefer it over
`math.log2` in competitive programming.
