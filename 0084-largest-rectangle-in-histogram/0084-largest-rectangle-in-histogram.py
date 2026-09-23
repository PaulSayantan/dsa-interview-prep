# ### Conceptual Breakdown
#
# Core Algorithmic Patterns:
# - Monotonic Increasing Stack
# - Previous Smaller Element
# - Next Smaller Element
# - Sentinel Value
# - Amortized Analysis
#
# Problem Thinking Process:
# - For any contiguous range of histogram bars:
#
#       area = minimum height in the range * width of the range
#
# - A brute-force solution examines every possible range and tracks its minimum height.
#   Since there are O(N^2) ranges, this approach is too slow for large inputs.
#
# - Instead of choosing every range, treat each bar as the possible shortest bar of
#   a rectangle.
#
# - For a bar at index `i` with height `h`, ask:
#
#       How far can a rectangle of height `h` extend to the left and right?
#
# - The rectangle can pass through every neighboring bar whose height is at least `h`.
#   It stops when it encounters a bar shorter than `h`.
#
# - Therefore, the widest rectangle controlled by bar `i` is bounded by:
#
#       left boundary  = nearest shorter bar on the left
#       right boundary = nearest shorter bar on the right
#
# - If these boundaries are at indices `left_smaller` and `right_smaller`, then:
#
#       usable indices = left_smaller + 1 ... right_smaller - 1
#       width          = right_smaller - left_smaller - 1
#       area           = heights[i] * width
#
# Mental Intuition & Logic:
# - Think of each bar in the stack as waiting to discover the first shorter bar
#   on its right.
#
# - The stack stores indices, not heights, because calculating the rectangle width
#   requires positions.
#
# - The heights represented by the stack remain in non-decreasing order:
#
#       heights[stack[0]] <= heights[stack[1]] <= ...
#
# - When the current bar is at least as tall as the stack's top bar, the top bar's
#   rectangle may still extend through it. We therefore keep the top bar in the stack.
#
# - When the current bar is shorter than the stack's top bar, the top bar cannot
#   extend through the current position. We pop it and calculate its rectangle.
#
# - At the moment a bar is popped:
#
#       current index `i` = first shorter boundary on the right
#       new stack top     = effective exclusive boundary on the left
#
# - Both boundaries are excluded from the rectangle, which explains the `-1`:
#
#       width = right_boundary - left_boundary - 1
#
# Example:
#
#       heights = [2, 1, 5, 6, 2, 3]
#       indices = 0 1 2 3 4 5
#
# - When we reach index 4, whose height is 2, the stack represents:
#
#       stack indices = [1, 2, 3]
#       stack heights = [1, 5, 6]
#
# - Height 2 is shorter than height 6, so height 6 is popped:
#
#       left boundary  = index 2
#       right boundary = index 4
#       width          = 4 - 2 - 1 = 1
#       area           = 6 * 1 = 6
#
# - Height 2 is also shorter than height 5, so height 5 is popped:
#
#       left boundary  = index 1
#       right boundary = index 4
#       width          = 4 - 1 - 1 = 2
#       area           = 5 * 2 = 10
#
# - The height-5 rectangle covers indices 2 and 3, whose heights are [5, 6].
#
# Breakdown of the Code Logic:
# 1. Create an empty stack for unresolved bar indices.
# 2. Scan the histogram from left to right.
# 3. Perform one extra iteration using an imaginary bar of height 0.
# 4. While the current bar is shorter than the stack-top bar:
#    a. Pop the taller bar.
#    b. Use the current index as its exclusive right boundary.
#    c. Use the new stack top as its exclusive left boundary.
#    d. Calculate its maximum width and area.
# 5. Push the current bar's index after restoring non-decreasing height order.
# 6. Return the largest area found.


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Returns the area of the largest rectangle that can be formed from
        consecutive histogram bars.

        Args:
            heights: The heights of histogram bars, each with width 1.

        Returns:
            The maximum rectangular area.

        Complexity:
            Time: O(N). Every bar is pushed once and popped at most once.
            Space: O(N) for the monotonic stack.
        """
        # The stack stores indices of bars that have not yet encountered
        # a strictly shorter bar on their right.
        stack: list[int] = []

        best_area = 0
        n = len(heights)

        # Include one extra iteration for an imaginary final bar of height 0.
        # This sentinel forces all remaining positive-height bars to be popped.
        for i in range(n + 1):
            current_height = 0 if i == n else heights[i]

            # The current bar blocks every taller bar at the top of the stack.
            # Pop those bars and calculate their widest known rectangles.
            while stack and heights[stack[-1]] > current_height:
                popped_index = stack.pop()
                rectangle_height = heights[popped_index]

                # The current index is the first strictly shorter bar
                # to the right of the popped bar.
                right_boundary = i

                # After popping, the new stack top is the exclusive left
                # boundary used for this rectangle.
                #
                # If the stack is empty, use -1 as an imaginary boundary
                # immediately before index 0.
                left_boundary = stack[-1] if stack else -1

                # Both boundary positions are excluded.
                rectangle_width = right_boundary - left_boundary - 1
                rectangle_area = rectangle_height * rectangle_width

                best_area = max(best_area, rectangle_area)

            # Do not store the imaginary sentinel index because it does not
            # correspond to an element inside `heights`.
            if i < n:
                stack.append(i)

        return best_area


# ### Reusable Patterns & Key Takeaways
#
# 1. Change the Viewpoint:
#    When checking every subarray or range is too expensive, consider treating each
#    element as the important or limiting element and calculate its best contribution.
#
# 2. Treat Each Bar as the Minimum:
#    Every valid rectangle has at least one shortest bar. By finding the widest
#    rectangle for every possible shortest bar, we cover the global optimum.
#
# 3. Previous Smaller and Next Smaller Elements:
#    A shorter bar blocks the chosen rectangle. The nearest shorter bars on both sides
#    determine the maximum width available to a chosen height.
#
# 4. Taller Bars Do Not Block the Rectangle:
#    A rectangle of height 5 can pass through a bar of height 6. It cannot pass through
#    a bar of height 4. This is why this problem needs smaller-element boundaries.
#
# 5. Store Indices When Distance Matters:
#    Heights alone are insufficient because the area also requires width. Indices let
#    us calculate distances and still retrieve heights from the input array.
#
# 6. Unresolved Candidates Belong in the Stack:
#    A bar remains in the stack while its rectangle might still expand to the right.
#    A future shorter bar resolves its missing right boundary.
#
# 7. Calculate an Element's Answer When It Is Popped:
#    The pop condition reveals the missing boundary. At that moment, enough information
#    exists to calculate the popped element's complete contribution.
#
# 8. Width Between Exclusive Boundaries:
#
#       width = right_boundary - left_boundary - 1
#
#    The `-1` excludes the shorter boundary bars from the rectangle.
#
# 9. Use a Sentinel to Flush Unresolved Elements:
#    An imaginary height-0 bar makes every remaining positive bar discover a right
#    boundary. This avoids duplicating the area calculation in a cleanup loop.
#
# 10. A Nested While Loop Can Still Be O(N):
#     Every index enters the stack once and leaves it at most once. Across the complete
#     algorithm, there are at most N pushes and N pops.
#
# 11. Equal-Height Policy Must Be Consistent:
#     This implementation pops only when the current height is strictly smaller (`>`).
#     Equal heights remain stacked. A later equal bar may receive a narrower rectangle,
#     while an earlier equal bar eventually receives the full available width.
#
# 12. Recognition Rule:
#     When a problem asks how far each value can extend before a smaller value blocks
#     it, consider a monotonic stack and Previous/Next Smaller Element boundaries.