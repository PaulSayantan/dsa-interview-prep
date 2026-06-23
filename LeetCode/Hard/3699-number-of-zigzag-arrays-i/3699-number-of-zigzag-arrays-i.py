"""
╔══════════════════════════════════════════════════════════════════════════════╗
║          3699. Number of ZigZag Arrays I  —  REVISION GUIDE                 ║
║          Difficulty: Hard  |  Tags: DP, Prefix Sum, Counting                ║
╚══════════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 SECTION 1 ─ UNDERSTANDING THE CONSTRAINT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  What does "no three consecutive strictly increasing/decreasing" actually mean?

  It means after every UP step, the next step MUST be DOWN.
  After every DOWN step, the next step MUST be UP.

  Valid shape:    UP → DOWN → UP → DOWN  (strict ZigZag — perfect alternation)
  Invalid shape:  UP → UP               (two ups in a row = strictly increasing triple)
  Invalid shape:  DOWN → DOWN           (two downs in a row = strictly decreasing triple)

  So the sequence shape looks like this when drawn:

       v      v         ← "peaks"
      / \    / \
     /   \  /   \
    /     \/     \
              ^         ← "valleys"

  ▸ Think of it as a signal: every rise is followed by a fall, every fall by a rise.
  ▸ Equal adjacent elements are also banned (first constraint), so every step changes value.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 SECTION 2 ─ WHY DP? DEFINING THE STATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  We build the array element by element. To decide what comes NEXT, we need
  two pieces of information about the current end of the sequence:
      1. What VALUE does it end with?      → determines valid next values
      2. What DIRECTION did it last move?  → determines the mandatory next direction

  Hence our DP state is a 2D table:

      dp[direction][value]  =  number of valid sequences of the current
                               length that end with `value` and last moved
                               in `direction`

  Directions:  UP   = last step was a strict increase
               DOWN = last step was a strict decrease

  Values are stored as 0-indexed offsets: index i maps to the actual value (l + i).
  Array size is m = r - l + 1.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 SECTION 3 ─ TRANSITION LOGIC (THE HEART OF THE DP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Ask: "How many ways can a sequence end at index v via an UP move?"

  To arrive at v via an UP move:
      → the previous value x must satisfy x < v      (strictly less, to go UP)
      → the previous direction must have been DOWN    (to alternate properly)

      new_dp_up[v] = Σ prev_dp_down[x]   for all x in [0, v-1]
                   = prefix_sum_of_down[v-1]

  To arrive at v via a DOWN move:
      → the previous value x must satisfy x > v      (strictly greater, to go DOWN)
      → the previous direction must have been UP      (to alternate properly)

      new_dp_down[v] = Σ prev_dp_up[x]   for all x in [v+1, m-1]
                     = total_up − prefix_sum_of_up[v]   (suffix sum trick)

  ┌──────────────────────────────────────────────────────────────────────────┐
  │  TRANSITION SUMMARY                                                      │
  │                                                                          │
  │  new_up[v]   =  prefix_down[v-1]          (sum of down[0..v-1])         │
  │  new_down[v] =  total_up - prefix_up[v]   (sum of up[v+1..m-1])         │
  └──────────────────────────────────────────────────────────────────────────┘

  Both transitions are now O(1) per value v — no inner loop needed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 SECTION 4 ─ BASE CASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  A sequence of length 1 hasn't made any move yet.
  Every value in [l, r] is a valid starting point.

  We initialize BOTH prev_up and prev_down to all 1s (not just one of them).

  Why both? Because a single-element sequence is a valid prefix for EITHER
  an upcoming UP or DOWN move. When we process the second element, we will
  look into prev_down (to compute new_up) and prev_up (to compute new_down).
  Seeding both with 1s correctly expresses that all m values are available
  as a foundation for either direction.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 SECTION 5 ─ DRY RUN  (n=3, l=1, r=3, so m=3, values: 0→1, 1→2, 2→3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ── AFTER LENGTH 1 (base case) ──
  prev_up   = [1, 1, 1]   (index: 0→val1, 1→val2, 2→val3)
  prev_down = [1, 1, 1]

  ── ITERATION 1: building sequences of length 2 ──

  Prefix sums:
      prefix_up   = [1, 2, 3]
      prefix_down = [1, 2, 3]
      total_up    = 3

  curr_up[v]   = prefix_down[v-1]  (sum of prev_down values strictly below v)
  curr_down[v] = total_up - prefix_up[v]   (sum of prev_up values strictly above v)

  v=0: curr_up[0]   = 0 (no index below 0)
       curr_down[0] = 3 - prefix_up[0] = 3 - 1 = 2
                     (sequences: 2→1, 3→1)

  v=1: curr_up[1]   = prefix_down[0] = 1
                     (sequences: 1→2)
       curr_down[1] = 3 - prefix_up[1] = 3 - 2 = 1
                     (sequences: 3→2)

  v=2: curr_up[2]   = prefix_down[1] = 2
                     (sequences: 1→3, 2→3)
       curr_down[2] = 3 - prefix_up[2] = 3 - 3 = 0
                     (no values above 3)

  After length 2:
  prev_up   = [0, 1, 2]
  prev_down = [2, 1, 0]

  ── ITERATION 2: building sequences of length 3 ──

  Prefix sums:
      prefix_up   = [0, 1, 3]
      prefix_down = [2, 3, 3]
      total_up    = 3

  v=0: curr_up[0]   = 0
       curr_down[0] = 3 - prefix_up[0] = 3 - 0 = 3
                     → endings at val=1 via DOWN: [2,1], [3,1], [2,3,1] wait...
                     (3 sequences ending at val1 via down = sum of up[1]+up[2] = 1+2 = 3)

  v=1: curr_up[1]   = prefix_down[0] = 2
                     (from down-ending sequences at val1: [2→1→2], [3→1→2])
       curr_down[1] = 3 - prefix_up[1] = 3 - 1 = 2
                     (from up-ending sequences at val3: [1→3→2], [2→3→2])

  v=2: curr_up[2]   = prefix_down[1] = 3
                     (from down-ending sequences at val1 or val2: [2→1→3],[3→1→3],[3→2→3])
       curr_down[2] = 3 - prefix_up[2] = 3 - 3 = 0

  After length 3:
  prev_up   = [0, 2, 3]
  prev_down = [3, 2, 0]

  Final answer = sum(prev_up) + sum(prev_down)
               = (0+2+3) + (3+2+0)
               = 5 + 5 = 10  ✓   (matches expected output)

  Cross-checking with the enumerated valid arrays from the problem:
  [1,2,1],[1,3,1],[1,3,2],[2,1,2],[2,1,3],[2,3,1],[2,3,2],[3,1,2],[3,1,3],[3,2,3]
  → 10 arrays. ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 SECTION 6 ─ COMPLEXITY ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Let m = r - l + 1  (number of distinct values available)

  ┌─────────────────────┬────────────────────────────────────────────────────┐
  │  Approach           │  Time              Space                           │
  ├─────────────────────┼────────────────────────────────────────────────────┤
  │  Naive DP           │  O(n × m²)         O(m)                           │
  │  (inner loop scan)  │  TLE for n,m=2000  (rolling arrays)               │
  ├─────────────────────┼────────────────────────────────────────────────────┤
  │  Optimized DP       │  O(n × m)          O(m)                           │
  │  (prefix sums)      │  ≈ 2000×2000 = 4M  (4 arrays of size m)           │
  └─────────────────────┴────────────────────────────────────────────────────┘

  The key optimization: instead of scanning all x < v (O(m) per v),
  we precompute the prefix sum array once per iteration (O(m)) and
  then answer each query in O(1).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 SECTION 7 ─ PATTERNS THIS PROBLEM EXEMPLIFIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ① Finite State Machine DP
     The problem bans "two of the same direction in a row". This is a
     sequence-level rule, not a value-level rule. Model it by making the
     DIRECTION an explicit DP state (UP / DOWN), then enforce alternation
     inside the transition formula. Pattern: whenever a constraint restricts
     which transitions are legal based on recent history, add that history
     as a state dimension.

  ② Prefix/Suffix Sum to Collapse an O(m) Inner Loop
     Transition required:  new_state[v] = Σ old_state[x]  over a range.
     Pattern: precompute prefix sums once → answer every range query in O(1).
     The suffix variant is just  total - prefix[v].
     Whenever your DP transition is "sum of all previous states up to/from a
     boundary", this optimization applies directly.

  ③ Coordinate Compression / Index Shifting
     Values live in [l, r] but array indices must start at 0.
     Map: index i  ↔  actual value (l + i).
     This avoids sparse arrays, prevents off-by-one boundary errors, and
     keeps memory proportional to the range size, not the max possible value.

  ④ Rolling Arrays (Space Optimization)
     The current row depends only on the previous row.
     Keep only two arrays (prev, curr) instead of the full n × m grid.
     Space drops from O(n × m) to O(m).
"""

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        # m = number of distinct usable values; indices [0..m-1] map to values [l..r]
        m = r - l + 1

        # ── BASE CASE ──────────────────────────────────────────────────────────
        # A single element is trivially valid; return m immediately.
        if n == 1:
            return m

        # Seed both arrays with 1s: every value can be a starting point for
        # either an upcoming UP or DOWN move (see Section 4 for why both).
        prev_up   = [1] * m   # prev_up[v]   = ways to reach value v via UP
        prev_down = [1] * m   # prev_down[v] = ways to reach value v via DOWN

        # ── MAIN LOOP ──────────────────────────────────────────────────────────
        # Process elements 2 through n (n-1 iterations total)
        for _ in range(1, n):

            # Step 1: Build prefix sum arrays for O(1) range queries
            prefix_up   = [0] * m
            prefix_down = [0] * m
            prefix_up[0]   = prev_up[0]
            prefix_down[0] = prev_down[0]
            for i in range(1, m):
                prefix_up[i]   = (prefix_up[i - 1]   + prev_up[i])   % MOD
                prefix_down[i] = (prefix_down[i - 1] + prev_down[i]) % MOD

            # total_up = sum of ALL prev_up entries; used to compute suffix sums
            total_up = prefix_up[-1]

            # Step 2: Compute the new DP states
            curr_up   = [0] * m
            curr_down = [0] * m

            for v in range(m):
                # curr_up[v]:   arrived here via UP from some x < v.
                #               Previous must have been DOWN (FSM rule).
                #               = sum of prev_down[0..v-1] = prefix_down[v-1]
                if v > 0:
                    curr_up[v] = prefix_down[v - 1]

                # curr_down[v]: arrived here via DOWN from some x > v.
                #               Previous must have been UP (FSM rule).
                #               = sum of prev_up[v+1..m-1]
                #               = total_up - prefix_up[v]
                curr_down[v] = (total_up - prefix_up[v]) % MOD

            # Step 3: Roll forward — discard the old row, keep the new one
            prev_up   = curr_up
            prev_down = curr_down

        # ── FINAL ANSWER ───────────────────────────────────────────────────────
        # Sum all ways to end a length-n sequence, regardless of final direction or value
        return (sum(prev_up) + sum(prev_down)) % MOD


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 QUICK REVISION FLASHCARDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Q: What are the two DP states and what do they track?
  A: prev_up[v]   = # valid sequences of current length ending at value v
                    where the LAST MOVE was an UP (increase).
     prev_down[v] = same but last move was DOWN (decrease).

  Q: Why initialize BOTH to [1]*m instead of just one?
  A: A single element has no prior direction. It can extend in either direction.
     Seeding both allows either prev_up or prev_down to be queried when
     building the second element.

  Q: Write the two transition formulas from memory.
  A: curr_up[v]   = prefix_down[v-1]       (no elements below index 0: → 0)
     curr_down[v] = total_up - prefix_up[v]

  Q: Why suffix sum instead of direct scan for curr_down?
  A: We need sum of prev_up[v+1..m-1]. Computing it as total - prefix_up[v]
     avoids scanning right to left or a separate suffix array.

  Q: What is the time complexity and why isn't it O(n*m²)?
  A: O(n*m). Each iteration computes prefix sums in O(m) and then fills
     curr_up/curr_down in O(m) using O(1) lookups. No inner loop.

  Q: What is coordinate compression doing here?
  A: Values l..r are mapped to indices 0..m-1. Saves memory, avoids
     empty array slots below l, and simplifies boundary logic.
"""