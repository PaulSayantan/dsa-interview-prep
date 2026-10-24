from typing import List

class Solution:
    """
    LeetCode 802: Find Eventual Safe States
    Link: https://leetcode.com/problems/find-eventual-safe-states/

    ============================================================================
    ### Conceptual Breakdown
    ============================================================================
    
    1. Core Algorithmic Pattern:
       - Directed Graph Cycle Detection via Depth-First Search (DFS) with 
         Three-Color State Coloring (White-Gray-Black Algorithm) / Memoization.
       - Alternative Pattern: Topological Sort (Kahn's Algorithm / BFS) on a 
         Reversed Graph using out-degrees (which become in-degrees upon reversal).

    2. Underlying Mental Intuition & Logic:
       - Problem Definition: A node is "safe" if EVERY possible path starting 
         from it eventually reaches a terminal node (a node with 0 outgoing edges).
       - The Contrapositive Insight: When does a path FAIL to reach a terminal 
         node? Only when it gets trapped in an infinite loop (a cycle). 
         In a finite directed graph, any path that does not terminate MUST 
         eventually revisit a node and form a cycle.
       - Reframing the Goal: 
         * Unsafe Node = Any node that is part of a cycle, OR has a directed 
           path leading into a cycle.
         * Safe Node   = Any node that is NOT part of a cycle and has NO paths 
           leading into a cycle.
       - Reaching the Optimal Solution:
         Instead of simulating every possible path from every node (which would 
         be exponential), we use DFS to detect cycles and memoize the state of 
         each node so we never process a node or edge more than once.
         
         While your two-array approach (`visited` and `path_visited`) works 
         great, we can optimize space and readability in interviews by merging 
         them into a single `state` array using 3 distinct states:
           * 0 (UNVISITED / White): Node has not been explored yet.
           * 1 (VISITING  / Gray) : Node is currently in the active recursion 
                                    stack. Encountering a node in state 1 means 
                                    we found a back-edge (a cycle!). Also acts 
                                    as the permanent marker for UNSAFE nodes if 
                                    we return early upon cycle detection.
           * 2 (SAFE      / Black): Node and all its descendants have been fully 
                                    explored without finding any cycles.
    ============================================================================
    """

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Identifies all eventual safe nodes in a directed graph, returned in 
        ascending order.

        Args:
            graph (List[List[int]]): A 0-indexed 2D adjacency list where graph[i] 
                                     contains the neighbors of node i.

        Returns:
            List[int]: A list of safe node indices sorted in ascending order.

        Complexity Analysis:
            - Time Complexity: O(V + E)
              Where V is the number of vertices (n) and E is the total number of 
              directed edges. Each vertex is transitioned through states 0 -> 1 -> 2 
              at most once, and each outgoing edge is inspected at most once.
            - Space Complexity: O(V)
              The `state` list requires O(V) auxiliary memory. The recursion 
              call stack takes up to O(V) space in the worst case (e.g., a 
              skewed line graph: 0 -> 1 -> 2 -> ... -> n-1).
        """
        n = len(graph)
        
        # State encoding for 3-color DFS:
        # 0 = Unvisited, 1 = Visiting (In current DFS path / Unsafe), 2 = Visited & Safe
        state = [0] * n

        def has_cycle(node: int) -> bool:
            """
            Helper DFS function that determines if `node` is part of a cycle 
            or leads to a cycle.

            Args:
                node (int): The current vertex being evaluated.

            Returns:
                bool: True if a cycle is reachable from `node` (making it unsafe), 
                      False if all paths from `node` safely terminate.
            """
            # Base Case 1: If the node is already evaluated, use memoized state.
            # - If state[node] == 1, we've looped back to an ancestor in the current 
            #   DFS path (cycle detected!), OR we hit a previously discovered unsafe node.
            # - If state[node] == 2, this node was already proven safe in an earlier branch.
            if state[node] != 0:
                return state[node] == 1

            # Mark node as 'Visiting' (1) as it enters the active recursion stack.
            state[node] = 1

            # Explore all outgoing edges (neighbors) from the current node.
            for neighbor in graph[node]:
                # If any neighbor leads to a cycle, the current node is also tainted (unsafe).
                # Notice we short-circuit and return True immediately!
                # Because we return early without updating state[node] to 2, 
                # state[node] remains 1, permanently memoizing this node as UNSAFE.
                if has_cycle(neighbor):
                    return True

            # Backtrack / Memoize as Safe:
            # If we exhausted all neighbors and none led to a cycle, this node 
            # (and all paths starting from it) is guaranteed to be safe.
            state[node] = 2
            return False

        # Iterate through all nodes from 0 to n - 1.
        # Because we iterate in natural order (0 -> n-1), our resulting list 
        # will automatically be sorted in ascending order without needing O(V log V) sorting.
        safe_nodes = []
        for i in range(n):
            if not has_cycle(i):
                safe_nodes.append(i)

        return safe_nodes


# ==============================================================================
# ### Reusable Patterns & Key Takeaways for Future Problem-Solving
# ==============================================================================
#
# 1. Two Arrays vs. Three-Color State Array:
#    - Using `visited` + `path_visited` (like in striver's problem video) is 100% 
#      valid and intuitive.
#    - Upgrading to a single `state` array (0 = Unvisited, 1 = Visiting/Unsafe, 
#      2 = Safe) is the industry-standard optimization for graph coloring. It 
#      halves the state-tracking arrays and makes base-case memoization cleaner.
#
# 2. The "Early Return" Memoization Trick:
#    - In standard backtracking, you reset `path_visited[node] = 0` after the loop.
#    - By returning `True` *before* resetting the state when a cycle is found, 
#      every node along the active recursive path stays marked as `1` (Unsafe). 
#      If another branch later touches any of those nodes, it immediately sees 
#      `state == 1` and returns in O(1) time instead of re-traversing the cycle!
#
# 3. Alternative Approach: Reverse Graph + Kahn's Algorithm (BFS):
#    - If an interviewer asks for an iterative solution (to avoid RecursionError 
#      on deep graphs), think from the terminal nodes backward:
#      a. Terminal nodes have an out-degree of 0 (guaranteed safe).
#      b. Reverse all edges in the graph. Now terminal nodes have an in-degree of 0.
#      c. Run standard Kahn's Topological Sort (BFS). Any node that eventually 
#         gets its in-degree reduced to 0 is a safe node; nodes stuck in cycles 
#         will never reach an in-degree of 0.
#
# 4. Related Problems Using This Exact Pattern:
#    - LeetCode 207: Course Schedule (Direct cycle detection in directed graph)
#    - LeetCode 210: Course Schedule II (Cycle detection + post-order reversal)
#    - LeetCode 2115: Find All Possible Recipes from Given Supplies
#    - LeetCode 2360: Longest Cycle in a Graph
# ==============================================================================